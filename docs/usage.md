---
title: Usage
jupytext:
  text_representation:
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Usage

## Familiarity with Open Source Tools

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
```

We asked respondents how familiar they are with the concepts of open source...

```{code-cell} ipython3
:tags: [remove-input]
# Software familiarity
familiarity_order = [
    'Extremely familiar',
    'Very familiar', 
    'Moderately familiar',
    'Slightly familiar',
    'Not familiar at all'
]

# Software (QID11)
df_f1 = (
    df.assign(
        QID4=df["QID4"].map(fill_unaffiliated),
        QID11=pd.Categorical(df["QID11"], categories=familiarity_order, ordered=True)
    )
    .rename(columns={"QID4": "Respondent Type"})
)

f1_df = (
    df_f1.groupby(["QID11", "Respondent Type"], observed=True, dropna=False)
         .size()
         .reset_index(name="Count")
)
f1_df["Percent"] = f1_df["Count"] / len(df)

# Hardware (QID10)
df_f2 = (
    df.assign(
        QID4=df["QID4"].map(fill_unaffiliated),
        QID10=pd.Categorical(df["QID10"], categories=familiarity_order, ordered=True)
    )
    .rename(columns={"QID4": "Respondent Type"})
)

f2_df = (
    df_f2.groupby(["QID10", "Respondent Type"], observed=True, dropna=False)
         .size()
         .reset_index(name="Count")
)
f2_df["Percent"] = f2_df["Count"] / len(df)

# Educational materials (QID12)
df_f3 = (
    df.assign(
        QID4=df["QID4"].map(fill_unaffiliated),
        QID12=pd.Categorical(df["QID12"], categories=familiarity_order, ordered=True)
    )
    .rename(columns={"QID4": "Respondent Type"})
)

f3_df = (
    df_f3.groupby(["QID12", "Respondent Type"], observed=True, dropna=False)
         .size()
         .reset_index(name="Count")
)
f3_df["Percent"] = f3_df["Count"] / len(df)
```


Examples of open source software include [Python](https://www.python.org/) and [git](https://git-scm.com/)

```{code-cell} ipython3
:tags: [remove-input]
fig1 = px.bar(
    f1_df, x="QID11", y="Percent",
    color="Respondent Type",
    barmode="stack",
    color_discrete_sequence=px.colors.qualitative.Plotly
)
fig1.update_layout(
    yaxis=dict(tickformat=".1%"),
    xaxis_title="",
    plot_bgcolor="white",
    paper_bgcolor="white"
)
fig1.show()
fig1.write_html('_static/familiarity_software.html', full_html=False, include_plotlyjs='cdn')
```

```{raw} html
:file: _static/familiarity_software.html
```

[Arduino boards](https://www.arduino.cc/) are an example of open source hardware

```{code-cell} ipython3
:tags: [remove-input]
fig2 = px.bar(
    f2_df, x="QID10", y="Percent",
    color="Respondent Type",
    barmode="stack",
    color_discrete_sequence=px.colors.qualitative.Plotly
)
fig2.update_layout(
    yaxis=dict(tickformat=".1%"),
    xaxis_title="",
    plot_bgcolor="white",
    paper_bgcolor="white"
)
fig2.show()
fig2.write_html('_static/familiarity_hardware.html', full_html=False, include_plotlyjs='cdn')
```

```{raw} html
:file: _static/familiarity_hardware.html
```

[Khan Academy](https://www.khanacademy.org/) and [MIT OpenCourseWare](https://ocw.mit.edu/) are examples of open source educational materials.

```{code-cell} ipython3
:tags: [remove-input]
fig3 = px.bar(
    f3_df, x="QID12", y="Percent",
    color="Respondent Type",
    barmode="stack",
    color_discrete_sequence=px.colors.qualitative.Plotly
)
fig3.update_layout(
    yaxis=dict(tickformat=".1%"),
    xaxis_title="",
    plot_bgcolor="white",
    paper_bgcolor="white"
)
fig3.show()
fig3.write_html('_static/familiarity_educational.html', full_html=False, include_plotlyjs='cdn')
```

```{raw} html
:file: _static/familiarity_educational.html
```


## What Open Source Tools Do Respondents Use?

```{code-cell} ipython3

os_tools_pct = prop(df["QID13"], lambda s: s == "Yes")
print(f"**{os_tools_pct}%** of respondents identified open source tools that are key in their workflows or their fields.")
```

Tools respondents identified included:

```{code-cell} ipython3
:tags: [remove-input]
# Text processing for word frequency analysis
rm_terms = {
    'open', 'and', 'source', 'analysis', 'use', 'used', 'data', 'many', 'software',
    'programming', 'language', 'languages', 'tools', 'code', 'etc', 'package',
    'packages', 'list', 'everything', 'including', 'libraries', 'like',
    'various', 'research', 'statistical', 'ecosystem', 'opensource', 'web',
    'google', 'system', 'compilers', 'academy', 'numerous', 'systems'
}

def clean_text(text):
    if pd.isna(text):
        return ""
    # Convert to lowercase and remove punctuation
    text = re.sub(r'[^\w\s]', ' ', text.lower())
    # Split into words and filter
    words = [word for word in text.split() 
             if word not in rm_terms and len(word) > 2]
    return ' '.join(words)

# Process text responses
tools_text = df['QID15'].dropna().apply(clean_text)
all_words = ' '.join(tools_text).split()
word_freq = Counter(all_words)

# Create dataframe for plotting
tools_highlight = ['python', 'r', 'julia', 'git', 'latex']
top_25_words = dict(word_freq.most_common(25))

tools_df = pd.DataFrame([
    {'word': word, 'freq': freq, 'pct': freq / len(df)}
    for word, freq in top_25_words.items()
    if word != '•'
]).sort_values('freq')

# Create lollipop plot
fig4 = go.Figure()

colors = ['#1f77b4' if word in tools_highlight else '#7f7f7f' 
          for word in tools_df['word']]

fig4.add_trace(go.Scatter(
    x=tools_df['pct'],
    y=tools_df['word'],
    mode='markers+lines',
    marker=dict(size=8, color=colors),
    line=dict(color='lightgray', width=1),
    orientation='h',
    hovertemplate='Tool: %{y}<br>Percent: %{x:.2%}<extra></extra>'
))

# Add line segments
for i, row in tools_df.iterrows():
    fig4.add_shape(
        type="line",
        x0=0, x1=row['pct'],
        y0=row['word'], y1=row['word'],
        line=dict(color=colors[i], width=2)
    )

fig4.update_layout(
    xaxis=dict(
        title="Responses Identifying Open Source Tool Use",
        tickformat='.0%'
    ),
    yaxis_title="",
    showlegend=False,
    plot_bgcolor="white",
    paper_bgcolor="white"
)
fig4.show()
fig4.write_html('_static/tools_lollipop.html', full_html=False, include_plotlyjs='cdn')
```

```{raw} html
:file: _static/tools_lollipop.html
```

Note that these are respondents' answers so not all tools may actually be open-source tools.

## How Are Respondents Using University-Provided Licensed Software?

We asked respondents which university-provided licensed software they use that are available in the university's software library.

```{code-cell} ipython3
:tags: [remove-input]
# Process licensed software responses
licensed_highlight = ['Matlab', 'STATA']

# Split comma-separated responses and count
licensed_tools = []
for response in df['QID17'].dropna():
    tools = [tool.strip() for tool in str(response).split(',')]
    licensed_tools.extend(tools)

licensed_freq = Counter(licensed_tools)
licensed_df = pd.DataFrame([
    {'tool': tool, 'freq': freq, 'pct': freq / len(df)}
    for tool, freq in licensed_freq.items()
]).sort_values('freq')

# Handle None/NaN values
if not licensed_df.empty:
    licensed_df = licensed_df[licensed_df['tool'] != 'nan']

# Create lollipop plot for licensed tools
fig5 = go.Figure()

colors_licensed = ['#1f77b4' if tool in licensed_highlight else '#7f7f7f' 
                   for tool in licensed_df['tool']]

fig5.add_trace(go.Scatter(
    x=licensed_df['pct'],
    y=licensed_df['tool'],
    mode='markers+lines',
    marker=dict(size=8, color=colors_licensed),
    line=dict(color='lightgray', width=1),
    orientation='h',
    hovertemplate='Tool: %{y}<br>Percent: %{x:.2%}<extra></extra>'
))

# Add line segments
for i, row in licensed_df.iterrows():
    fig5.add_shape(
        type="line",
        x0=0, x1=row['pct'],
        y0=row['tool'], y1=row['tool'],
        line=dict(color=colors_licensed[i], width=2)
    )

fig5.update_layout(
    xaxis=dict(
        title="Responses Identifying Licensed Tool Use",
        tickformat='.0%'
    ),
    yaxis_title="",
    showlegend=False,
    plot_bgcolor="white",
    paper_bgcolor="white"
)
fig5.show()
fig5.write_html('_static/licensed_tools.html', full_html=False, include_plotlyjs='cdn')
```

```{raw} html
:file: _static/licensed_tools.html
```

## Usage of Open Source Tools vs. Licensed Tools

Additionally, we asked respondents if they use open-source tools more than, as much as, or less than the licensed software provided by the university.

```{code-cell} ipython3
:tags: [remove-input]
# Clean and categorize usage comparison responses
usage_mapping = {
    'I use open source software much more than the licensed software in CSL': 'Use OS more than licensed',
    'I use open source software much less than the licensed software in CSL': 'Use OS less than licensed', 
    'I use open source software about the same as the licensed software in CSL': 'About the same',
    'N/A, I don\'t use either': 'Use neither'
}

usage_order = [
    'Use OS more than licensed',
    'About the same',
    'Use OS less than licensed', 
    'Use neither'
]

df_u1 = (
    df.assign(
        QID4=df["QID4"].map(fill_unaffiliated),
        QID40_clean=df["QID40"].map(lambda x: usage_mapping.get(x, x)),
        QID40_clean_cat=pd.Categorical(
            df["QID40"].map(lambda x: usage_mapping.get(x, x)), 
            categories=usage_order, 
            ordered=True
        )
    )
    .rename(columns={"QID4": "Respondent Type"})
)

u1_df = (
    df_u1.groupby(["QID40_clean_cat", "Respondent Type"], observed=True, dropna=False)
         .size()
         .reset_index(name="Count")
)

fig6 = px.bar(
    u1_df, x="QID40_clean_cat", y="Count",
    color="Respondent Type",
    barmode="stack",
    color_discrete_sequence=px.colors.qualitative.Plotly
)
fig6.update_layout(
    xaxis_title="",
    plot_bgcolor="white",
    paper_bgcolor="white"
)
fig6.show()
fig6.write_html('_static/usage_comparison.html', full_html=False, include_plotlyjs='cdn')
```

```{raw} html
:file: _static/usage_comparison.html
```