import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency, mannwhitneyu, ttest_ind, norm

# Define your functions here
def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    df = df.drop_duplicates()
    numerical_columns = df.select_dtypes(include=['number']).columns
    categorical_columns = df.select_dtypes(include=['object']).columns

    df[numerical_columns] = df[numerical_columns].fillna(df[numerical_columns].median())
    for column in categorical_columns:
        df[column] = df[column].fillna(df[column].mode()[0])

    return df

def merge_data(df_demo, df_experiment, df_combined):
    df_demo.columns = df_demo.columns.str.strip().str.lower()
    df_experiment.columns = df_experiment.columns.str.strip().str.lower()
    df_combined.columns = df_combined.columns.str.strip().str.lower()

    merged_df = pd.merge(df_demo, df_experiment, on='client_id', how='inner')
    merged_df = pd.merge(merged_df, df_combined, on='client_id', how='inner')
    return merged_df

def compute_chi_square(df, col1, col2):
    observed = pd.crosstab(df[col1], df[col2])
    chi2, p, dof, expected = chi2_contingency(observed)
    return chi2, p

def compute_mannwhitneyu(group1, group2):
    u_stat, p_value = mannwhitneyu(group1, group2)
    return u_stat, p_value

def compute_ttest(group1, group2):
    t_stat, p_value = ttest_ind(group1, group2)
    return t_stat, p_value

def z_test_for_proportions(success_a, size_a, success_b, size_b):
    prop_a = success_a / size_a
    prop_b = success_b / size_b
    pooled_prop = (success_a + success_b) / (size_a + size_b)
    se = np.sqrt(pooled_prop * (1 - pooled_prop) * (1/size_a + 1/size_b))
    z_score = (prop_b - prop_a) / se
    p_value = 1 - norm.cdf(z_score)
    return z_score, p_value
