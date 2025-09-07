---
title: Perceptions
jupytext:
  text_representation:
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

```{code-cell} ipython3
:tags: [remove-input]
# Imports
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import plotly.io as pio
import matplotlib as mpl
import numpy as np
from collections import Counter
import re

from setup import *

df = survey_results
```

# Value of Open Source Projects
When asked to characterize the importance of open source tools to their education, teaching, and research, respondents said the following:


```{code-cell} ipython3
:tags: [remove-input]
# Software familiarity
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Create the equivalent of your R pipeline
s1_df = (
    survey_results.assign(
        QID4=survey_results["QID4"].fillna("Unaffiliated"),  # equivalent to ifelse(is.na(QID4), 'Unaffiliated', QID4)
        QID16=pd.Categorical(
            survey_results["QID16"], 
            categories=[
                'Critical/Vital/Essential',
                'Valuable', 
                'Neutral',
                'Little importance',
                'Irrelevant'
            ], 
            ordered=True
        )
    )
    .rename(columns={"QID4": "Respondent Type"})  # equivalent to rename()
    .groupby(["QID16", "Respondent Type"], observed=True, dropna=False)  # group_by()
    .size()  # equivalent to summarise(Count = n())
    .reset_index(name="Count")
)

# Calculate percentage
s1_df["Percent"] = s1_df["Count"] / len(survey_results)

# Create the plot using plotly express (simpler than go.Figure)
fig = px.bar(
    s1_df, 
    x="QID16", 
    y="Percent",
    color="Respondent Type",
    barmode="stack"
)

# Update layout to match your styling
fig.update_layout(
    xaxis=dict(title=""),
    yaxis=dict(
        zerolinecolor="#ffffff",
        zerolinewidth=2,
        gridcolor="#ffffff",
        tickformat=".1%"
    )
)

fig.show()
fig.write_html('_static/perceptions.html', full_html=False, include_plotlyjs='cdn')
```

```{raw} html
:file: _static/perceptions.html
```

Survey takers were also asked how much they agree that 1) open source tools are a valuable form of research output and 2) open source tools are an important way to translate research into entrepreneurship and innovation.

```{code-cell} ipython3
:tags: [remove-input]

# Create the equivalent of your R pipeline
s4 = (
    survey_results[["ResponseId", "QID18"]]  # select()
    .assign(QID18=survey_results["QID18"].astype(str))  # ensure string type
    .assign(QID18=lambda df: df["QID18"].str.split(','))  # prepare for explode
    .explode("QID18")  # equivalent to separate_rows()
    .assign(QID18=lambda df: df["QID18"].str.strip())  # remove whitespace
    .groupby("QID18", dropna=False)  # group_by()
    .size()  # equivalent to summarise(count = n())
    .reset_index(name="count")
    .rename(columns={"QID18": "Benefit"})
    .assign(pct=lambda df: df["count"] / len(survey_results))  # calculate percentage
    .assign(Benefit=lambda df: df["Benefit"].fillna("None"))  # handle NAs
    .sort_values("pct", ascending=False)  # arrange(desc(pct))
)

# Create lollipop plot
fig = go.Figure()

# Add only the markers (no connecting lines between different categories)
fig.add_trace(go.Scatter(
    x=s4["pct"],
    y=s4["Benefit"],
    mode='markers',  # Changed from 'lines+markers' to just 'markers'
    marker=dict(size=8, color=PRIMARY_COLOR),
    orientation='h',
    hovertemplate='%{y}<br>%{x:.2%}<extra></extra>',
    showlegend=False
))

# Add individual line segments for lollipop effect (from 0 to each point)
for i, row in s4.iterrows():
    fig.add_shape(
        type="line",
        x0=0, x1=row["pct"],
        y0=row["Benefit"], y1=row["Benefit"],
        line=dict(color=PRIMARY_COLOR, width=2)
    )

# Update layout
fig.update_layout(
    xaxis=dict(
        title="Percent of Respondents Agreeing with Benefits of Using Open Source Software",
        tickformat=".1%",
        range=[0, 1]
    ),
    yaxis=dict(
        title="",
        categoryorder="array",
        categoryarray=s4.sort_values("pct")["Benefit"].tolist()
    ),
    showlegend=False
)


fig.write_html('_static/benefits.html', full_html=False, include_plotlyjs='cdn')
```
## Benefits of Open Source Tools in Academic Settings

We asked survey respondents to choose among a list of potential benefits of using open-source tools in their work. Of the survey-takers who identified benefits, the percentage of respondents who identified each benefit are shown below:

```{raw} html
:file: _static/benefits.html
```