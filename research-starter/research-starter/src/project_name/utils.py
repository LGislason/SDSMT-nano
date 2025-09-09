
from pathlib import Path
import pandas as pd

def summary_table(df: pd.DataFrame) -> pd.DataFrame:
    """Return a simple summary table for a DataFrame."""
    return df.describe(include="all").T
