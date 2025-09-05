# From here https://github.com/UW-Madison-DSI/open_source_survey_results/blob/main/setup.R to python
# --- Setup ----------------------------------------------------
from pathlib import Path
import pandas as pd
import plotly.express as px
import plotly.io as pio
import matplotlib as mpl

# ===== Colors / branding (R → Python) =====
PRIMARY_COLOR      = "#9B0000"   # UW-Madison primary
DARK_ACCENT        = "#333333"
BACKGROUND_COLOR   = "#F7F7F7"
UNI_NAME           = "UW-Madison"

# ===== Plotly theme (rough analog to your ggplot2 themes) =====
# See: https://plotly.com/python/templates/
pio.templates["uw_theme"] = pio.templates["plotly_white"].layout.update(
    {
        "font": {"family": "Red Hat Text, Arial, sans-serif"},
        "paper_bgcolor": BACKGROUND_COLOR,
        "plot_bgcolor": BACKGROUND_COLOR,
        "colorway": [PRIMARY_COLOR, "#666666", "#B60205", "#8c1515", "#9c9c9c"],
        "legend": {"orientation": "h", "yanchor": "bottom", "y": -0.2},
        "xaxis": {"gridcolor": "rgba(0,0,0,0)"},
        "yaxis": {"gridcolor": DARK_ACCENT},
    }
)
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
    }
)

# --- Data loading & cleaning ----------------------------------

DATA = "data/survey_data.csv"
template_df = pd.read_csv(DATA, nrows=1)
survey_template = (
    template_df.iloc[0]
    .to_frame(name="q_text")
    .reset_index()
    .rename(columns={"index": "q_number"})
)

survey_results = pd.read_csv(DATA, header=None, skiprows=3)

# Drop last 2 rows (R: tail(-2))
survey_results = survey_results.iloc[:-2].copy()

# 3) Assign column names from the "q_number" vector we captured
survey_results.columns = survey_template["q_number"].tolist()

# 4) Keep complete responses only (R: filter(Finished == TRUE))
finished_col = "Finished"      # <-- EDIT THIS if your column is named differently
if finished_col in survey_results.columns:
    survey_results = survey_results[survey_results[finished_col] == True].copy()
else:
    raise KeyError(
        f"Column '{finished_col}' not found. Update 'finished_col' to your exact header."
    )

# Preview a few columns/rows
survey_template.head(3), survey_results.head(3)
