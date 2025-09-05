---
title: Usage
---

# Usage

This page summarizes responses about open source *usage* (tools, languages, practices).

:::{note}
Keep `data/` paths the same; plots below assume the existing CSVs.
:::

```{code-cell} python
import pandas as pd
import plotly.express as px

df = pd.read_csv("data/tool_usage.csv")  # example file name
fig = px.bar(df, x="tool", y="count", title="Reported Tool Usage")
fig.show()
```
