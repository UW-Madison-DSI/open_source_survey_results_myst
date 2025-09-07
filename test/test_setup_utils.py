import math
import pandas as pd
import numpy as np

# Import your helper module used across pages
# (Repo uses `from setup import *` in pages; here we import it directly)
import setup  # noqa: F401

def test_fill_unaffiliated_maps_nan_to_label():
    assert setup.fill_unaffiliated(np.nan) == "Unaffiliated"
    assert setup.fill_unaffiliated("Faculty") == "Faculty"

def test_prop_basic_percentage():
    s = pd.Series(["Yes", "No", "Yes", "No", "Yes"])
    pct_yes = setup.prop(s, lambda x: x == "Yes")
    # 3/5 = 0.6 -> 60
    assert pct_yes == 60

def test_prop_handles_empty_series():
    s = pd.Series([], dtype="object")
    pct = setup.prop(s, lambda x: x == "Yes")
    # Should not crash; expect 0.0%
    assert pct == 0.0

def test_prop_ignores_nas():
    s = pd.Series(["Yes", None, "No", np.nan, "Yes"])
    pct_yes = setup.prop(s, lambda x: x == "Yes")
    # Non-NA values are 3: ["Yes","No","Yes"] → 2/3 ≈ 0.6667 → 66
    assert pct_yes == 66
