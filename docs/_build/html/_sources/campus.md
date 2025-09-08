---
title: Campus Culture
jupytext:
  text_representation:
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Campus Culture

## Perceptions of Open Source Culture On Campus

```{code-cell} ipython3
:tags: [remove-input]
# Imports
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import plotly.io as pio
import matplotlib as mpl
from myst_nb import glue
from setup import *

df = survey_results

# Compute & glue (no visible output)
valuable_pct = int(100 * df['QID24'].eq("Very valuable").mean())
_ = glue("valuable_pct", valuable_pct, display=False)  # prevents display

# Figure
qid24_order = ["Very valuable","Some value","Neutral","No value"]
df_c1 = (
    df.assign(
        QID4=df["QID4"].map(fill_unaffiliated),
        QID24=pd.Categorical(df["QID24"], categories=qid24_order, ordered=True)
    )
    .rename(columns={"QID4": "Respondent Type"})
)
c1_df = (
    df_c1.groupby(["QID24", "Respondent Type"], observed=True, dropna=False)
         .size()
         .reset_index(name="Count")
)
c1_df["Percent"] = c1_df["Count"] / len(df)

fig1 = px.bar(
    c1_df, x="QID24", y="Percent",
    color="Respondent Type",
    barmode="stack",
    title='"Do you see value in having a vibrant culture around open source software?"'
)
fig1.update_layout(yaxis=dict(tickformat=".1%"), xaxis_title="", plot_bgcolor="white", paper_bgcolor="white")
fig1  # let Jupyter-Book render the figure
fig1.write_html('_static/plotly_example.html', full_html=False, include_plotlyjs='cdn')
```
**{glue:}`valuable_pct`%** of respondents said that having a vibrant open source culture is **“very valuable”**.

```{raw} html
:file: _static/plotly_example.html
```


```{code-cell} ipython3
:tags: [remove-input]
agree_options = {"Strongly agree", "Somewhat agree"}
```

```{code-cell} ipython3
:tags: [remove-input]
# ----- Figure 2: "There is a vibrant culture at UNI" by Respondent Type -----


agree_vibrant = round(100 * df['QID23'].isin(["Strongly agree","Somewhat agree"]).mean(),2)
_ = glue("agree_vibrant", agree_vibrant, display=False)  # prevents display

qid23_order = [
    "Strongly agree",
    "Somewhat agree", 
    "Neither agree nor disagree",
    "Somewhat disagree",
    "Strongly disagree",
]
df_c2 = (
    df.assign(
        QID4=df["QID4"].map(fill_unaffiliated),
        QID23=pd.Categorical(df["QID23"], categories=qid23_order, ordered=True)
    )
    .rename(columns={"QID4": "Respondent Type"})
)

pct_makes_sense = round(
    100 * df['QID23'].isin([
        "Strongly agree",
        "Somewhat agree",
        "Neither agree nor disagree"
    ]).mean(), 2)
_ = glue("pct_makes_sense", pct_makes_sense, display=False)  # prevents display

c2_df = (
    df_c2.groupby(["QID23", "Respondent Type"], observed=True, dropna=False)
         .size()
         .reset_index(name="Count")
)
c2_df["Percent"] = c2_df["Count"] / len(df)

fig2 = px.bar(
    c2_df, x="QID23", y="Percent",
    color="Respondent Type",
    barmode="stack",
    title='"The university has a vibrant open source culture"'
)
fig2.update_layout(
    yaxis=dict(tickformat=".1%"),
    xaxis_title="",
    plot_bgcolor="white",
    paper_bgcolor="white"
)
fig2.write_html('_static/fig2.html', full_html=False, include_plotlyjs='cdn')
```

In comparison, only **{glue:}`agree_vibrant`%** agreed that there is a vibrant open source culture at UW-Madison.

```{raw} html
:file: _static/fig2.html
```
**{glue:}`pct_makes_sense`%** of respondents agreed that **“it makes sense for the university to contribute to open source software that is vital to its educational and research enterprise”**.

## Open Source Training On Campus



```{code-cell} ipython3
:tags: [remove-input]
# QID25 == "Yes" for received at least some formal training
training_yes_pct = prop(df["QID25"], lambda s: s == "Yes")

received_training = int(100*df['QID25'].eq("Yes").astype(int).mean())
_ = glue("received_training", received_training, display=False)  # prevents display


df_c3 = (
    df.assign(
        QID4=df["QID4"].map(fill_unaffiliated)
    )
    .rename(columns={"QID4": "Respondent Type"})
)
c3_df = (
    df_c3.groupby(["QID25", "Respondent Type"], observed=True, dropna=False)
         .size()
         .reset_index(name="Count")
)
c3_df["Percent"] = c3_df["Count"] / len(df)

df_c4 = (
    df.assign(
        QID8=df["QID8"].map(fill_unaffiliated)
    )
    .rename(columns={"QID8": "Affiliation"})
)
c4_df = (
    df_c4.groupby(["QID25", "Affiliation"], observed=True, dropna=False)
         .size()
         .reset_index(name="Count")
)
c4_df["Percent"] = c4_df["Count"] / len(df)
```
**{glue:}`received_training`%** of respondents said that they have received at least some formal training or education on open source software during their time at UW-Madison. These respondents were distributed by role and affiliation as below:

### Training by Role

```{code-cell} ipython3
:tags: [remove-input]
fig3 = px.bar(
    c3_df, x="QID25", y="Percent",
    color="Respondent Type",
    barmode="stack",
    title="Have received open source training at the university (by role)"
)
fig3.update_layout(
    yaxis=dict(tickformat=".1%"),
    xaxis_title="",
    plot_bgcolor="white",
    paper_bgcolor="white",
)
fig3.show()
fig3.write_html('_static/fig3.html', full_html=False, include_plotlyjs='cdn')
```

```{raw} html
:file: _static/fig3.html
```

### Training by Affiliation

```{code-cell} ipython3
:tags: [remove-input]
fig4 = px.bar(
    c4_df, x="QID25", y="Percent",
    color="Affiliation",
    barmode="stack", 
    title="Have received open source training at the university (by affiliation)"
)
fig4.update_layout(
    yaxis=dict(tickformat=".1%"),
    xaxis_title="",
    plot_bgcolor="white",
    paper_bgcolor="white"
)
fig4.update_layout(hoverlabel=dict(namelength=-1))
fig4.show()  # This was missing!
fig4.write_html('_static/fig4.html', full_html=False, include_plotlyjs='cdn')



```

```{raw} html
:file: _static/fig4.html
```

```{code-cell} ipython3
:tags: [remove-input]
# Interest in more training (QID28) and OSPO workshops (QID29)
more_training_pct = prop(df["QID28"], lambda s: s == "Yes")
ospo_workshops_pct = prop(df["QID29"], lambda s: s == "Yes")
_1 = glue("more_training_pct", more_training_pct, display=False)  # prevents display
_2 = glue("ospo_workshops_pct", ospo_workshops_pct, display=False)  # prevents display

```

**{glue:}`more_training_pct`%** of respondents said that they “would like to see more training, education, or support for learning how to contribute to open source project” and **{glue:}`ospo_workshops_pct`%** of respondents expressed interest in potential open source training sessions and workshops organized by the Open Source Program Office.
