import pandas as pd
from scipy.stats import chi2_contingency, mannwhitneyu
import matplotlib.pyplot as plt
import seaborn as sns

# Function to read data
def read_data(file_path, delimiter='\t'):
    return pd.read_csv(file_path, sep=delimiter)

# Function to clean the data
def clean_data(df):
    df = df.drop_duplicates()
    numerical_columns = df.select_dtypes(include=['number']).columns
    categorical_columns = df.select_dtypes(include=['object']).columns
    df[numerical_columns] = df[numerical_columns].fillna(df[numerical_columns].median())
    for column in categorical_columns:
        df[column] = df[column].fillna(df[column].mode()[0])
    return df

# Function to merge datasets
def merge_datasets(df1, df2, on='client_id', how='inner'):
    return pd.merge(df1, df2, on=on, how=how)

# Function to calculate completion rates
def calculate_completion_rate(df):
    total = df.shape[0]
    completed = df[df['process_step'] == 'confirm'].shape[0]
    return completed / total

# Function for hypothesis test on completion rates
def hypothesis_test_completion_rate(df):
    control_group = df[df['Variation'] == 'Control']
    test_group = df[df['Variation'] == 'Test']
    control_completed = control_group[control_group['process_step'] == 'confirm'].shape[0]
    control_total = control_group.shape[0]
    test_completed = test_group[test_group['process_step'] == 'confirm'].shape[0]
    test_total = test_group.shape[0]
    observed = [[control_completed, control_total - control_completed],
                [test_completed, test_total - test_completed]]
    chi2, p_value, _, _ = chi2_contingency(observed)
    return chi2, p_value

# Function for hypothesis test on time spent
def hypothesis_test_time_spent(df):
    df['date_time'] = pd.to_datetime(df['date_time'], errors='coerce')
    df.sort_values(by=['client_id', 'date_time'], inplace=True)
    df['dwell_time'] = df.groupby('client_id')['date_time'].diff().dt.total_seconds()
    df.dropna(subset=['dwell_time'], inplace=True)
    control_dwell_time = df[df['Variation'] == 'Control']['dwell_time']
    test_dwell_time = df[df['Variation'] == 'Test']['dwell_time']
    u_stat, p_value = mannwhitneyu(control_dwell_time, test_dwell_time)
    return u_stat, p_value

# Function for hypothesis test on error rates
def hypothesis_test_error_rate(df):
    control_group = df[df['Variation'] == 'Control']
    test_group = df[df['Variation'] == 'Test']
    control_errors = control_group[control_group['process_step'] != 'confirm'].shape[0]
    control_total = control_group.shape[0]
    test_errors = test_group[test_group['process_step'] != 'confirm'].shape[0]
    test_total = test_group.shape[0]
    observed_errors = [[control_errors, control_total - control_errors],
                       [test_errors, test_total - test_errors]]
    chi2_errors, p_value_errors, _, _ = chi2_contingency(observed_errors)
    return chi2_errors, p_value_errors

# Plotting functions for EDA
def plot_age_distribution(df):
    sns.histplot(df['clnt_age'], kde=True, color='green')
    plt.title('Distribution of Client Age')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()

def plot_gender_distribution(df):
    sns.boxenplot(data=df, x="gendr", y="clnt_tenure_yr", palette='Set1')
    plt.title('Client Tenure Distribution by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Tenure (Years)')
    plt.show()

def plot_login_distribution(df):
    sns.histplot(df['logons_6_mnth'], kde=True, color='green')
    plt.title('Number of Logins in the Last 6 Months')
    plt.xlabel('Number of Logins')
    plt.ylabel('Frequency')
    plt.show()

def plot_call_distribution(df):
    sns.histplot(df['calls_6_mnth'], kde=True, color='orange')
    plt.title('Number of Calls in the Last 6 Months')
    plt.xlabel('Number of Calls')
    plt.ylabel('Frequency')
    plt.show()
