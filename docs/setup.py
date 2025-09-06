# docs/setup.py
from pathlib import Path
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import matplotlib as mpl

# ===== Colors / branding =====
PRIMARY_COLOR      = "#9B0000"   # UW-Madison primary
DARK_ACCENT        = "#333333"
BACKGROUND_COLOR   = "#F7F7F7"
UNI_NAME           = "UW-Madison"

# ===== Plotly theme: define overrides as a named template =====
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

# Register overrides and set default as a *string* combination
pio.templates["uw_overrides"] = uw_overrides
pio.templates.default = "plotly_white+uw_overrides"   # <-- key change, no Template addition

# ===== Matplotlib defaults (optional) =====
mpl.rcParams.update({
    "figure.facecolor": BACKGROUND_COLOR,
    "axes.facecolor": BACKGROUND_COLOR,
    "axes.edgecolor": DARK_ACCENT,
    "axes.titleweight": "bold",
    "axes.labelcolor": DARK_ACCENT,
    "xtick.color": DARK_ACCENT,
    "ytick.color": DARK_ACCENT,
})

# ===== Load your data once here if you want to `from setup import *` =====
# Adjust the path to your CSV as needed or read it upstream and pass it in.
DATA_PATH = Path(__file__).resolve().parents[1] / "data" / "survey_data.csv"
survey_results = pd.read_csv(DATA_PATH)
