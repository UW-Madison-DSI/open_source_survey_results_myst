---
title: Demographics
jupytext:
  text_representation:
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Demographics


```{code-cell} ipython3
:tags: [remove-input]
# Imports
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from pathlib import Path
from setup import *  # provides survey_results, colors, etc.
import plotly.express as px
import re

# Data
df = survey_results.copy()

# Child rows: (type=QID4, division=QID8)
child = (
    df.groupby(["QID4", "QID8"], dropna=False)
      .size()
      .reset_index(name="n")
      .rename(columns={"QID4": "type", "QID8": "division"})
)
child["type"] = child["type"].fillna("Unaffiliated")
child["division"] = child["division"].fillna("Unaffiliated")

# Parent rows: totals per type (as "division" label; parent type empty later)
parent = (
    df.groupby(["QID4"], dropna=False)
      .size()
      .reset_index(name="n")
      .rename(columns={"QID4": "division"})
)
parent["division"] = parent["division"].fillna("Unaffiliated")
parent["type"] = pd.NA
parent = parent[["type", "division", "n"]]

# Combine + ids/parents
plot_df = pd.concat([child[["type", "division", "n"]], parent], ignore_index=True)
plot_df["ids"] = np.where(
    plot_df["type"].isna(),
    plot_df["division"],
    plot_df["type"].astype(str) + "_" + plot_df["division"].astype(str)
)
plot_df["type"] = plot_df["type"].fillna("")   # root parent is ""
plot_df["n"] = plot_df["n"].astype(float)

# Figure
fig = go.Figure(go.Treemap(
    labels=plot_df["division"],
    parents=plot_df["type"],
    ids=plot_df["ids"],
    values=plot_df["n"],
    branchvalues="total",
    hoverinfo="text",
    hovertemplate="<b>%{parent}</b><br>Type: %{label}<br>Responses: %{value}<extra></extra>",
    textposition="middle center",
    textfont=dict(size=14),
))
fig.update_layout(
    title="Survey Respondents"
)
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))


out_html = "_static/role_demogr.html"
fig.write_html(out_html, full_html=False, include_plotlyjs="cdn")
```

323 respondents finished the survey, broken out by role and affiliation below.

### Role
```{raw} html
:file: _static/role_demogr.html
```

### Affiliation

```{code-cell} ipython3
:tags: [remove-input]
# Imports

# --- 1) Child rows: counts by (type=QID4, division=QID8) ---
child = (
    df.groupby(["QID4", "QID8"], dropna=False)
      .size()
      .reset_index(name="n")
      .rename(columns={"QID4": "type", "QID8": "division"})
)

# Label NA as "Unaffiliated" for display consistency
child["type"] = child["type"].fillna("Unaffiliated")
child["division"] = child["division"].fillna("Unaffiliated")

# --- 2) Parent rows: totals for each division (R code: group_by(type = QID8)) ---
parent = (
    df.groupby(["QID8"], dropna=False)
      .size()
      .reset_index(name="n")
      .rename(columns={"QID8": "type"})  # <- parent label lives in `type`
)
parent["type"] = parent["type"].fillna("Unaffiliated")
parent["division"] = pd.NA  # parent rows have no parent (root)

parent = parent[["type", "division", "n"]]

# --- 3) Bind, build ids, clean for Plotly ---
plot_df = pd.concat([child[["type", "division", "n"]], parent], ignore_index=True)

# ids: if division is NA -> id = type; else id = f"{division}_{type}"
plot_df["ids"] = np.where(
    plot_df["division"].isna(),
    plot_df["type"].astype(str),
    plot_df["division"].astype(str) + "_" + plot_df["type"].astype(str),
)

# Plotly expects empty-string for root parents (not NA)
plot_df["division"] = plot_df["division"].fillna("")
plot_df["type"] = plot_df["type"].fillna("")
plot_df["n"] = plot_df["n"].astype(float)

# --- 4) Treemap (labels=type, parents=division) ---
fig = go.Figure(go.Treemap(
    labels=plot_df["type"],
    parents=plot_df["division"],
    ids=plot_df["ids"],
    values=plot_df["n"],
    branchvalues="total",
    hoverinfo="text",
    hovertemplate="<b>%{parent}</b><br>Type: %{label}<br>Responses: %{value}<extra></extra>",
    textinfo="label+value",
    textposition="middle center",  # valid Plotly value
    textfont=dict(size=14),
))

fig.update_layout(
    title="Survey Respondents",
    plot_bgcolor=BACKGROUND_COLOR,
    paper_bgcolor=BACKGROUND_COLOR,
    margin=dict(t=60, l=0, r=0, b=0),
)
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

out_html = "_static/afiliation_demogr.html"
fig.write_html(out_html, full_html=False, include_plotlyjs="cdn")
```

```{raw} html
:file: _static/afiliation_demogr.html
```


```{code-cell} ipython3
:tags: [remove-input]
df_rt = df.copy()
df_rt["Respondent Type"] = df_rt["QID4"].fillna("Unaffiliated")

total_n = len(df_rt)
c1_df = (
    df_rt.groupby(["QID22", "Respondent Type"], dropna=False)
          .size()
          .reset_index(name="Count")
)
c1_df["Percent"] = c1_df["Count"] / total_n
c1_df["QID22"] = c1_df["QID22"].fillna("Missing")

# Plot
fig = px.bar(
    c1_df,
    x="QID22",
    y="Percent",
    color="Respondent Type"
)

fig.update_layout(
    barmode="stack",
    title="Have contributed to open source projects?",
    xaxis_title="Have contributed to open source projects?",
    yaxis=dict(
        zerolinecolor="#ffffff",
        zerolinewidth=2,
        gridcolor="#ffffff",
        tickformat=".1%",
        title=None
    ),
    legend_title_text="Respondent Type",
    margin=dict(t=60, l=0, r=0, b=0),
)
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))


Path("_static").mkdir(exist_ok=True, parents=True)
fig.write_html("_static/contrib_by_type.html", full_html=False, include_plotlyjs="cdn")
```

53% of respondents said they have contributed to open source projects, either academically or personally.

```{raw} html
:file: _static/contrib_by_type.html
```

## Faculty and Staff

```{code-cell} ipython3
:tags: [remove-input]
levels_qid6 = ['0-1 years', '1-3 years', '4-7 years', '7-10 years', '10+ years']

df_ten = survey_results.copy()

# Keep only Faculty & Staff
df_ten = df_ten[df_ten["QID4"].isin(["Faculty", "Staff"])].copy()

# Make QID6 categorical with your level order
df_ten["QID6"] = pd.Categorical(df_ten["QID6"], categories=levels_qid6, ordered=True)

# Count per facet (QID4) and tenure bucket (QID6)
counts = (
    df_ten.groupby(["QID4", "QID6"], observed=True, dropna=False)
          .size()
          .reset_index(name="Count")
)

# Ensure every (QID4, QID6) pair appears (even if zero) so facets align
full_index = (
    pd.MultiIndex.from_product(
        [counts["QID4"].unique(), levels_qid6],
        names=["QID4", "QID6"]
    )
)
counts = (
    counts.set_index(["QID4", "QID6"])
          .reindex(full_index, fill_value=0)
          .reset_index()
)

# Plot: horizontal bars, facet per QID4, reverse y-order
fig = px.bar(
    counts,
    x="Count",
    y="QID6",
    facet_col="QID4",
    orientation="h",
    category_orders={"QID6": list(reversed(levels_qid6))},  # reverse like scale_y_discrete(limits = rev)
    color_discrete_sequence=[PRIMARY_COLOR],
)

# Style & tooltip (count)
fig.update_traces(
    marker_line_color="white",
    marker_line_width=0.5,
    hovertemplate="Years Served: %{y}<br>Count: %{x}<extra></extra>"
)

fig.update_layout(
    title="Years Served (Faculty vs Staff)",
    bargap=0.2,
    showlegend=False,
    margin=dict(t=60, l=20, r=20, b=40),
)
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

# Axis labels like your labs()
fig.for_each_yaxis(lambda a: a.update(title_text="Years Served"))
fig.for_each_xaxis(lambda a: a.update(title_text="Respondents"))

# Optional: save for Jupyter-Book embed
from pathlib import Path
Path("_static").mkdir(exist_ok=True, parents=True)
fig.write_html("_static/tenure_faculty_staff.html", full_html=False, include_plotlyjs="cdn")

```
Of these respondents, 230 identified as faculty or staff (71% of respondents).

Faculty and staff respondents were distributed in tenure (years served) at the university as below:
```{raw} html
:file: _static/tenure_faculty_staff.html
```

## Students
75 respondents identified at students (23% of respondents). Students came from degree programs in the following subjects:

```{code-cell} ipython3
:tags: [remove-input]
df_maj = df.copy()
df_maj = df_maj[df_maj["QID4"].isin(["Graduate Student", "Undergraduate Student"])].copy()
df_maj["QID4"] = df_maj["QID4"].map(
    {"Graduate Student": "Graduate", "Undergraduate Student": "Undergraduate"}
)

# --- 2) Clean major text (QID7) ---
def clean_major(x: str) -> str:
    if pd.isna(x):
        return "Not Provided"
    s = str(x)
    s = s.title()                    # to Title Case
    s = s.replace("&", "And")        # '&' -> 'And'
    s = re.sub(r"\s*Phd\b", "", s, flags=re.IGNORECASE)  # remove ' Phd' (case-insensitive)
    return s.strip() or "Not Provided"

df_maj["QID7"] = df_maj["QID7"].apply(clean_major)

# Manual recodes to match R's case_when
recode = {
    "Ag And Applied Economics": "Applied And Agricultural Economics",
    "Communication Sciences And Disorders (Csd)": "Communication Sciences And Disorders",
    "Computer Sciences": "Computer Science",
    "Industrial And Systems Engineering Phd": "Industrial & Systems Engineering",
    "Math": "Mathematics",
    "Nurtritional Sciences": "Nutrition Science",
}
df_maj["QID7"] = df_maj["QID7"].replace(recode)

# Ensure NAs → 'Not Provided'
df_maj["QID7"] = df_maj["QID7"].fillna("Not Provided")

# --- 3) Count majors per role ---
counts = (
    df_maj.groupby(["QID4", "QID7"], dropna=False)
          .size()
          .reset_index(name="Count")
)

# Global ordering of majors by frequency (to mimic reorder(QID7, QID7, length))
order_global = (
    counts.groupby("QID7")["Count"].sum()
          .sort_values(ascending=True)               # ascending → bottom-to-top small→large after flip
          .index.tolist()
)

# --- 4) Plot (horizontal, facet by QID4), single color, count tooltip ---
fig = px.bar(
    counts,
    x="Count",
    y="QID7",
    facet_col="QID4",
    orientation="h",
    category_orders={"QID7": order_global},  # global order across facets
)

fig.update_traces(
    marker_color=PRIMARY_COLOR,
    marker_line_color="white",
    marker_line_width=0.5,
    hovertemplate="Major: %{y}<br>Count: %{x}<extra></extra>",
    showlegend=False,
)

# Labels & theme (akin to labs + coord_flip theme)
fig.update_layout(
    title="Student Majors (Graduate vs Undergraduate)",
    bargap=0.2,
    margin=dict(t=60, l=40, r=20, b=40),
)
fig.for_each_annotation(lambda a: a.update(text=a.text.split("=")[-1]))

fig.for_each_yaxis(lambda a: a.update(title_text="Major"))
fig.for_each_xaxis(lambda a: a.update(title_text="Respondents"))


# Optional: save for Jupyter-Book embed
from pathlib import Path
Path("_static").mkdir(exist_ok=True, parents=True)
fig.write_html("_static/students_demog.html", full_html=False, include_plotlyjs="cdn")

```
53% of respondents said they have contributed to open source projects, either academically or personally.

```{raw} html
:file: _static/students_demog.html
```