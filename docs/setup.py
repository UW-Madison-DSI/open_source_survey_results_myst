# From here https://github.com/UW-Madison-DSI/open_source_survey_results/blob/main/setup.R to python
# --- Setup ----------------------------------------------------
from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import matplotlib as mpl

# ===== Colors / branding (R → Python) =====
PRIMARY_COLOR      = "#9B0000"   # UW-Madison primary
DARK_ACCENT        = "#333333"
BACKGROUND_COLOR   = "#F7F7F7"
UNI_NAME           = "UW-Madison"

# ===== Plotly theme (fix: use a Template and merge with base) =====
uw_overrides = go.layout.Template(
    layout=go.Layout(
        font=dict(family="Red Hat Text, Arial, sans-serif"),
        paper_bgcolor=BACKGROUND_COLOR,
        plot_bgcolor=BACKGROUND_COLOR,
        colorway=[PRIMARY_COLOR, "#666666", "#B60205", "#8c1515", "#9c9c9c"],
        legend=dict(orientation="h", yanchor="bottom", y=-0.2),
        xaxis=dict(gridcolor="rgba(0,0,0,0)", automargin=True, zerolinecolor="#EBF0F8", zerolinewidth=2),
        yaxis=dict(gridcolor=DARK_ACCENT, automargin=True, zerolinecolor="#EBF0F8", zerolinewidth=2),
        hovermode="closest",
        title=dict(x=0.05),
    )
)
pio.templates["uw_theme"] = pio.templates["plotly_white"] + uw_overrides
pio.templates.default = "uw_theme"

# ===== Matplotlib defaults (if you make static figures too) =====
# rcParams guide: https://matplotlib.org/stable/users/explain/customizing.html
mpl.rcParams.update(
    {
        "figure.facecolor": BACKGROUND_COLOR,
        "axes.facecolor": BACKGROUND_COLOR,
        "axes.edgecolor": DARK_ACCENT,
        "axes.grid": True,
        "grid.color": DARK_ACCENT,
        "grid.alpha": 1.0,
        "legend.framealpha": 1.0,
        "font.family": "sans-serif",
        "font.sans-serif": ["Red Hat Text", "Arial", "DejaVu Sans"],
    }
)

# --- Data loading & cleaning ----------------------------------
# Qualtrics CSVs often have 2 metadata rows, then a row of question text, then a row of export tags.
# Your R code used: first row for question numbers text, then data from row 4 (skiprows=3), and dropped last 2 rows.

DATA = "data/survey_data.csv"

def _read_first_nonempty_row(csv_path: str, row_idx: int) -> pd.Series:
    df = pd.read_csv(csv_path, nrows=1, skiprows=row_idx)
    return df.iloc[0]

def _try_load_columns(csv_path: str):
    """
    Try a couple of common Qualtrics layouts to recover column names and data:
    - Pattern A (your current): first row are 'q_number' style headers; data starts after 3 rows.
    - Pattern B (Qualtrics default): 2 meta rows, then export tags row; data starts after 2 rows.
    Returns (columns_list, data_df)
    """
    # Pattern A: your current approach (skip first 3 lines for data)
    try:
        first_row = pd.read_csv(csv_path, nrows=1)  # raw first row (question numbers or text)
        survey_template = (
            first_row.iloc[0].to_frame(name="q_text").reset_index().rename(columns={"index": "q_number"})
        )
        cols = survey_template["q_number"].tolist()

        data_df = pd.read_csv(csv_path, header=None, skiprows=3)
        # drop potential trailing summary rows (2 is common); guard if fewer rows
        if len(data_df) >= 2:
            data_df = data_df.iloc[:-2].copy()
        data_df.columns = cols
        return cols, data_df, survey_template
    except Exception:
        pass

    # Pattern B: use the third row (after two meta rows) as headers directly
    try:
        data_df = pd.read_csv(csv_path, skiprows=2)  # this row becomes header automatically
        cols = list(data_df.columns)
        survey_template = (
            pd.Series(cols, name="q_number").to_frame().assign(q_text=None).reset_index(drop=True)
        )
        return cols, data_df, survey_template
    except Exception as e:
        raise RuntimeError(f"Unable to parse Qualtrics CSV headers. Last error: {e}")

# Load template + data
_columns, _df, survey_template = _try_load_columns(DATA)
survey_results = _df.copy()

# Keep complete responses only (R: filter(Finished == TRUE))
finished_col = "Finished"  # change here if your column name differs
if finished_col in survey_results.columns:
    # Handle possible string "True"/"FALSE" variants
    finished_vals = survey_results[finished_col]
    if finished_vals.dtype == object:
        survey_results = survey_results[
            finished_vals.astype(str).str.lower().isin({"true", "t", "1", "yes"})
        ].copy()
    else:
        survey_results = survey_results[finished_vals == True].copy()
else:
    # If Finished column is truly absent, leave data as-is but warn in a comment
    # (avoids raising during book build)
    pass

# --- Helpers exposed for downstream notebooks -----------------
def prop(series: pd.Series, condition) -> float:
    """Percent (0-100) of entries in `series` that satisfy `condition(series)`."""
    s = series.dropna()
    if len(s) == 0:
        return 0.0
    return round(s[condition(s)].shape[0] / len(s) * 100, 2)

def fill_unaffiliated(x):
    return "Unaffiliated" if (pd.isna(x) or str(x).strip() == "") else x