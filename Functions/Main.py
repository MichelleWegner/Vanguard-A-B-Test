# main.py
import pandas as pd
from functions import load_data, combine_data, clean_data, remove_outliers, chi_square_test, mann_whitney_u_test, z_test_proportion
import Functions.eda as eda

# Load and combine data
file_paths = ['data/Clean_Data.csv']
df_list = load_data(file_paths)
df_combined = combine_data(df_list)

# Clean data
clean_df = clean_data(df_combined)
clean_df = remove_outliers(clean_df, 'bal')

# Perform EDA
eda.plot_age_distribution(clean_df)
eda.plot_gender_distribution(clean_df)
eda.plot_tenure_distribution(clean_df)
eda.plot_login_frequency(clean_df)
eda.plot_call_frequency(clean_df)

# Hypothesis Tests
# 1. Completion rate
control_group = clean_df[clean_df['variation'] == 'Control']
test_group = clean_df[clean_df['variation'] == 'Test']

control_completed = control_group[control_group['process_step'] == 'confirm'].shape[0]
control_total = control_group.shape[0]

test_completed = test_group[test_group['process_step'] == 'confirm'].shape[0]
test_total = test_group.shape[0]

chi2, p_value, dof, expected = chi_square_test(control_completed, control_total, test_completed, test_total)
print(f"Chi-square value: {chi2}, p-value: {p_value}, dof: {dof}")

# 2. Length of stay
control_dwell_time = control_group['dwell_time']
test_dwell_time = test_group['dwell_time']

u_stat, p_value = mann_whitney_u_test(control_dwell_time, test_dwell_time)
print(f"U-statistic value: {u_stat}, p-value: {p_value}")

# 3. Error rates
control_errors = control_group[control_group['process_step'] != 'confirm'].shape[0]
test_errors = test_group[test_group['process_step'] != 'confirm'].shape[0]

chi2_errors, p_value_errors, dof_errors, expected_errors = chi_square_test(control_errors, control_total, test_errors, test_total)
print(f"Chi-square value: {chi2_errors}, p-value: {p_value_errors}, dof: {dof_errors}")

# 4. Completion rate with cost-effectiveness threshold
z_score, p_value = z_test_proportion(control_completed, control_total, test_completed, test_total, threshold=0.05)
print(f"Z-score: {z_score}, P-value: {p_value}")