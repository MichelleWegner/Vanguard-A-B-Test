# main.py

from data_processing import load_data, clean_data, convert_to_numeric, remove_outliers
from eda import summarize_data, calculate_distributions
from metrics import calculate_completion_rate, calculate_error_rate
from hypothesis_testing import chi_square_test, mann_whitney_u_test, z_test
from visualization import plot_histogram, plot_boxplot
from models import train_logistic_regression
import config.settings as settings

# Load data
df = load_data(settings.DATA_PATH)

# Clean data
df = clean_data(df)
df = convert_to_numeric(df, ['clnt_age', 'num_accts', 'bal', 'calls_6_mnth', 'logons_6_mnth'])
df = remove_outliers(df, 'bal')

# EDA
summarize_data(df)
calculate_distributions(df, 'gendr')

# Metrics
completion_rate = calculate_completion_rate(df)
error_rate = calculate_error_rate(df)

# Hypothesis testing
control_group = df[df['variation'] == 'Control']
test_group = df[df['variation'] == 'Test']
observed = [[control_group.shape[0], test_group.shape[0]]]
chi2, p_value, dof, expected = chi_square_test(observed)

# Visualization
plot_histogram(df, 'clnt_age', 'Age Distribution')
plot_boxplot(df, 'gendr', 'clnt_tenure_yr', 'Tenure by Gender')

# Modeling
train_logistic_regression(df, 'process_step')
