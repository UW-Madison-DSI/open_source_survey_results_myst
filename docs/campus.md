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

# Perceptions of Open Source Culture On Campus

## Value of Open Source Culture
```{code-cell} ipython3
:tags: [hide-input]
# Imports
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import plotly.io as pio
import matplotlib as mpl

from setup import *
# Load data (adjust path if needed)
df = survey_results

# Helper: safe proportion
def prop(series, condition):
    series = series.dropna()
    if len(df) == 0:
        return 0.0
    return round((series[condition(series)].shape[0]) / len(df), 2) * 100

# Clean label helpers
def fill_unaffiliated(x):
    return "Unaffiliated" if pd.isna(x) else x

very_valuable_pct = prop(df["QID24"], lambda s: s == "Very valuable")
print(f"Percentage who find vibrant culture 'Very valuable': {very_valuable_pct}%")

# ----- Figure 1: "Value of a vibrant culture" by Respondent Type -----

# Map / order categories to match your R code
qid24_order = [
    "Very valuable",
    "Some value", 
    "Neutral",
    "No value"
]
df_c1 = (
    df.assign(
        QID4=df["QID4"].map(fill_unaffiliated),
        QID24=pd.Categorical(df["QID24"], categories=qid24_order, ordered=True)
    )
    .rename(columns={"QID4": "Respondent Type"})
)

# Group and compute percentages over all responses (like your R code)
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
fig1.update_layout(
    yaxis=dict(tickformat=".1%"),
    xaxis_title="",
    plot_bgcolor="white",
    paper_bgcolor="white"
)
fig1.show()
fig1.write_html('_static/plotly_example.html', full_html=False, include_plotlyjs='cdn')
```

```{raw} html
:file: _static/plotly_example.html
```

## Current Campus Culture Perception

```{code-cell} ipython3
:tags: [hide-input]
agree_options = {"Strongly agree", "Somewhat agree"}
vibrant_agree_pct = prop(df["QID23"], lambda s: s.isin(agree_options))

print(f"In comparison, only **{vibrant_agree_pct}%** agreed that there is a vibrant open source culture at the university.")
```

```{code-cell} ipython3
:tags: [remove-input]
# ----- Figure 2: "There is a vibrant culture at UNI" by Respondent Type -----

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
fig2.show()  # This was missing!
fig2.write_html('_static/fig2.html', full_html=False, include_plotlyjs='cdn')
```

```{raw} html
:file: _static/fig2.html
```

## University Contribution to Open Source

```{code-cell} ipython3
:tags: [remove-input]
# Agreement about contributing to OSS being sensible for the university
yes_pct = prop(df["QID19"], lambda s: s == "Yes")
unsure_pct = prop(df["QID19"], lambda s: s == "Not sure")
no_pct = prop(df["QID19"], lambda s: s == "No")

print(f"Should the university contribute to open source:")
print(f"- Yes: {yes_pct}%")
print(f"- Not sure: {unsure_pct}%") 
print(f"- No: {no_pct}%")
```

## Open Source Training On Campus

```{code-cell} ipython3
:tags: [remove-input]
# QID25 == "Yes" for received at least some formal training
training_yes_pct = prop(df["QID25"], lambda s: s == "Yes")
print(f"Percentage who have received open source training: {training_yes_pct}%")

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

## Interest in Additional Training

```{code-cell} ipython3
:tags: [remove-input]
# Interest in more training (QID28) and OSPO workshops (QID29)
more_training_pct = prop(df["QID28"], lambda s: s == "Yes")
ospo_workshops_pct = prop(df["QID29"], lambda s: s == "Yes")

print(f"Interest in more training: {more_training_pct}%")
print(f"Interest in OSPO workshops: {ospo_workshops_pct}%")
```