# setup.py
from pathlib import Path
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import matplotlib as mpl

# ========= Branding / colors =========
PRIMARY_COLOR    = "#9B0000"   # UW–Madison primary
DARK_ACCENT      = "#333333"
BACKGROUND_COLOR = "#F7F7F7"
UNI_NAME         = "UW-Madison"

# ========= Plotly theme =========
# Define your overrides as a named Template and combine via string
uw_overrides = go.layout.Template(
    layout=go.Layout(
        font=dict(family="Red Hat Text, Arial, sans-serif"),
        paper_bgcolor=BACKGROUND_COLOR,
        plot_bgcolor=BACKGROUND_COLOR,
        colorway=[PRIMARY_COLOR, "#666666", "#B60205", "#8c1515", "#9c9c9c", "#c2c2c2"],
        legend=dict(title=None, bgcolor="rgba(0,0,0,0)"),
        margin=dict(l=40, r=20, t=60, b=40),
        xaxis=dict(gridcolor="#e9e9e9", zeroline=False),
        yaxis=dict(gridcolor="#e9e9e9", zeroline=False),
        title=dict(x=0.01, xanchor="left"),
    )
)
pio.templates["uw_overrides"] = uw_overrides
pio.templates.default = "plotly_white+uw_overrides"  # works across Plotly versions

# ========= Matplotlib defaults (for static figs if needed) =========
mpl.rcParams.update({
    "figure.facecolor": BACKGROUND_COLOR,
    "axes.facecolor": BACKGROUND_COLOR,
    "axes.edgecolor": DARK_ACCENT,
    "axes.titleweight": "bold",
    "axes.labelcolor": DARK_ACCENT,
    "xtick.color": DARK_ACCENT,
    "ytick.color": DARK_ACCENT,
    "axes.grid": True,
    "grid.color": "#e9e9e9",
    "grid.linestyle": "-",
    "grid.linewidth": 0.6,
})

# ========= Data loading & cleaning =========
# Mirrors the R:
# - First read gets the header row with question text (1st row)
# - Second read gets the data: header=None, skip first 3 lines, drop last 2 rows
DATA_PATH = "data/survey_data.csv"

# 1) Extract survey "template" (question text in row 1)
#    Equivalent to: survey_template <- survey_df[1,] |> pivot_longer(...)
#    Here we read only the first row (nrows=1) then pivot to (q_number, q_text)
_template_row = pd.read_csv(DATA_PATH, nrows=1)
survey_template = (
    _template_row.T
    .reset_index()
    .rename(columns={"index": "q_number", 0: "q_text"})
)

# 2) Extract survey results, keeping complete responses only
#    Equivalent to:
#    survey_results <- read_csv(..., col_names = FALSE, skip = 3) |> tail(-2)
#    colnames(survey_results) <- survey_template$q_number
survey_results = pd.read_csv(DATA_PATH, header=None, skiprows=3)
# Drop last 2 rows like R's tail(-2)
if len(survey_results) >= 2:
    survey_results = survey_results.iloc[:-2, :]

# Apply header names from the template q_number
survey_results.columns = survey_template["q_number"].tolist()

# If the CSV has a Finished column as logical in R, it's likely "TRUE"/"FALSE" strings.
# Normalize to boolean and filter Finished == TRUE
if "Finished" in survey_results.columns:
    # Coerce to boolean (case-insensitive)
    survey_results["Finished"] = (
        survey_results["Finished"].astype(str).str.strip().str.lower().isin(["true", "t", "1", "yes"])
    )
    survey_results = survey_results[survey_results["Finished"] == True].copy()

# ========= Small utilities to mimic your helpers =========
def prop(series: pd.Series, predicate) -> float:
    """Safe percentage over full df length; predicate takes the series and returns a boolean mask."""
    s = series.dropna()
    denom = len(survey_results)
    if denom == 0:
        return 0.0
    num = s[predicate(s)].shape[0]
    return round((num / denom) * 100, 2)

def fill_unaffiliated(x):
    return "Unaffiliated" if pd.isna(x) or str(x).strip() == "" else x

# Export names commonly imported via `from setup import *`
__all__ = [
    "PRIMARY_COLOR", "DARK_ACCENT", "BACKGROUND_COLOR", "UNI_NAME",
    "survey_template", "survey_results",
    "prop", "fill_unaffiliated",
]