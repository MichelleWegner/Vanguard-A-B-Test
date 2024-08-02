# functions.py
import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, mannwhitneyu, zscore, norm

def load_data(file_paths):
    dfs = [pd.read_csv(file_path, sep=",") for file_path in file_paths]
    return dfs

def combine_data(dfs):
    df_combined = pd.concat(dfs)
    return df_combined

def clean_data(df):
    # Standardize column names
    df.columns = df.columns.str.strip().str.lower()
    
    # Drop rows with missing values
    df = df.dropna()
    
    # Remove duplicates
    df = df.drop_duplicates()
    
    # Ensure numerical and categorical data types are correct
    numerical_columns = ['clnt_age', 'num_accts', 'bal', 'calls_6_mnth', 'logons_6_mnth']
    df[numerical_columns] = df[numerical_columns].apply(pd.to_numeric, errors='coerce')
    df['gendr'] = df['gendr'].astype('category')
    
    return df

def remove_outliers(df, column):
    df[f'{column}_zscore'] = zscore(df[column])
    df = df[(df[f'{column}_zscore'] >= -3) & (df[f'{column}_zscore'] <= 3)]
    df = df.drop(columns=[f'{column}_zscore'])
    return df

def chi_square_test(control_completed, control_total, test_completed, test_total):
    control_not_completed = control_total - control_completed
    test_not_completed = test_total - test_completed

    observed = [[control_completed, control_not_completed],
                [test_completed, test_not_completed]]
    
    chi2, p_value, dof, expected = chi2_contingency(observed)
    return chi2, p_value, dof, expected

def mann_whitney_u_test(control, test):
    u_stat, p_value = mannwhitneyu(control, test)
    return u_stat, p_value

def z_test_proportion(control_success, control_total, test_success, test_total, threshold=0.05):
    control_prop = control_success / control_total
    test_prop = test_success / test_total

    pooled_prop = (control_success + test_success) / (control_total + test_total)
    se = np.sqrt(pooled_prop * (1 - pooled_prop) * (1/control_total + 1/test_total))
    z_score = (test_prop - control_prop - threshold) / se

    p_value = 1 - norm.cdf(z_score)
    return z_score, p_value
