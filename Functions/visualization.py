# visualization.py

import matplotlib.pyplot as plt
import seaborn as sns

def plot_histogram(df, column, title):
    """Plot histogram for a given column."""
    sns.histplot(df[column], kde=True)
    plt.title(title)
    plt.show()

def plot_boxplot(df, x, y, title):
    """Plot boxplot for given x and y."""
    sns.boxenplot(data=df, x=x, y=y)
    plt.title(title)
    plt.show()
