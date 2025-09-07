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
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path
import plotly.io as pio
import matplotlib as mpl
import numpy as np
from collections import Counter
import re
from myst_nb import glue
from setup import *

df = survey_results

import pandas as pd
import numpy as np
import plotly.graph_objects as go

# --- Inputs ---
# survey_results: your DataFrame with columns QID4 (type) and QID8 (division)
BACKGROUND_COLOR = "#F7F7F7"  # or whatever you use

df = survey_results.copy()

# 1) Child rows: counts by (type=QID4, division=QID8)
child = (
    df.groupby(["QID4", "QID8"], dropna=False)
      .size()
      .reset_index(name="n")
      .rename(columns={"QID4": "type", "QID8": "division"})
)

# Replace NaN with "Unaffiliated" **for labels only** (keeps structure clean)
child["type"] = child["type"].fillna("Unaffiliated")
child["division"] = child["division"].fillna("Unaffiliated")

# 2) Parent rows: totals for each type (as “division” label; parent’s `type` left NA)
parent = (
    df.groupby(["QID4"], dropna=False)
      .size()
      .reset_index(name="n")
      .rename(columns={"QID4": "division"})
)
parent["division"] = parent["division"].fillna("Unaffiliated")
parent["type"] = pd.NA  # becomes the root/parent (empty string) later
parent = parent[["type", "division", "n"]]

# 3) Bind rows and build ids/parents
plot_df = pd.concat(
    [child[["type", "division", "n"]], parent],
    ignore_index=True
)

# ids: parent rows get id = division; child rows get "type_division"
plot_df["ids"] = np.where(
    plot_df["type"].isna(),
    plot_df["division"],
    plot_df["type"].astype(str) + "_" + plot_df["division"].astype(str)
)

# parents: root for parent rows = "" (empty string)
plot_df["type"] = plot_df["type"].fillna("")  # Plotly wants "" for root
plot_df["n"] = plot_df["n"].astype(float)

# 4) Treemap
fig = go.Figure(
    go.Treemap(
        labels=plot_df["division"],
        parents=plot_df["type"],
        ids=plot_df["ids"],
        values=plot_df["n"],
        branchvalues="total",
        hoverinfo="text",
        hovertemplate="<b>%{parent}</b><br>Type: %{label}<br>Responses: %{value}<extra></extra>",
        textposition="middle",
        textfont=dict(size=14),
    )
)

fig.update_layout(
    title="Survey Respondents",
    plot_bgcolor=BACKGROUND_COLOR,
    paper_bgcolor=BACKGROUND_COLOR,
    margin=dict(t=60, l=0, r=0, b=0)
)

fig.show()

fig1.write_html('_static/afiliation_demogr.html', full_html=False, include_plotlyjs='cdn')


```

```{raw} html
:file: _static/afiliation_demogr.html
```

## Faculty and Staff

## Students
