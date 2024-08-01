# eda.py

import pandas as pd

def summarize_data(df):
    """Print summary statistics and data types of the dataframe."""
    print(df.describe())
    print(df.dtypes)

def calculate_distributions(df, column):
    """Calculate and return value counts for a given column."""
    return df[column].value_counts()
