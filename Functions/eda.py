# eda.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_age_distribution(df, younger_threshold=40):
    younger_clients = df[df['clnt_age'] < younger_threshold]
    older_clients = df[df['clnt_age'] >= younger_threshold]

    plt.figure(figsize=(10, 6))
    sns.histplot(younger_clients['clnt_age'], kde=True, color='blue', label='Younger Clients')
    sns.histplot(older_clients['clnt_age'], kde=True, color='red', label='Older Clients')
    plt.title('Age Distribution: Younger vs Older Clients')
    plt.xlabel('Client Age')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_gender_distribution(df):
    plt.figure(figsize=(14, 7))
    sns.boxenplot(data=df, x="gendr", y="clnt_tenure_yr", palette='Set1')
    plt.title('Client Tenure Distribution by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Tenure (Years)')
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)
    plt.show()

def plot_tenure_distribution(df, tenure_threshold=5):
    new_clients = df[df['clnt_tenure_yr'] < tenure_threshold]
    long_standing_clients = df[df['clnt_tenure_yr'] >= tenure_threshold]

    plt.figure(figsize=(10, 6))
    sns.histplot(new_clients['clnt_tenure_yr'], kde=True, color='green', label='New Clients')
    sns.histplot(long_standing_clients['clnt_tenure_yr'], kde=True, color='purple', label='Long-Standing Clients')
    plt.title('Account Age Distribution: New vs Long-Standing Clients')
    plt.xlabel('Client Tenure (Years)')
    plt.ylabel('Frequency')
    plt.legend()
    plt.grid(True)
    plt.show()

def plot_login_frequency(df):
    logins = df['logons_6_mnth'].value_counts().sort_index()
    cumulative_logins = logins.cumsum()

    plt.figure(figsize=(10, 6))
    plt.step(cumulative_logins.index, cumulative_logins, where='mid', color='green')
    plt.title('Cumulative Number of Logins in the Last 6 Months')
    plt.xlabel('Number of Logins')
    plt.ylabel('Cumulative Frequency')
    plt.grid(True)
    plt.show()

def plot_call_frequency(df):
    calls = df['calls_6_mnth'].value_counts().sort_index()

    plt.figure(figsize=(10, 6))
    plt.plot(calls.index, calls, marker='o', color='orange')
    plt.title('Frequency of Calls in the Last 6 Months')
    plt.xlabel('Number of Calls')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()
