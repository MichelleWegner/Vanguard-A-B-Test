import pandas as pd

def load_data(file_path):
    """Load dataset from the given file path."""
    return pd.read_csv(file_path)

def clean_data(df):
    """Clean and prepare the data for analysis."""
    df = df.dropna()  # Drop rows with missing values
    df = df.drop_duplicates()  # Remove duplicates
    df['gendr'] = df['gendr'].astype('category')
    df = df[df['gendr'].isin(['M', 'F'])]  # Filter invalid gender entries
    df = df.dropna(subset=['gendr'])
    return df

def convert_to_numeric(df, columns):
    """Convert specified columns to numeric data types."""
    df[columns] = df[columns].apply(pd.to_numeric, errors='coerce')
    return df

def remove_outliers(df, column):
    """Remove outliers based on z-scores for a given column."""
    df['zscore'] = (df[column] - df[column].mean()) / df[column].std()
    df = df[(df['zscore'] >= -3) & (df['zscore'] <= 3)]
    df = df.drop(columns=['zscore'])
    return df
