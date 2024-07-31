from function import load_data, clean_data, merge_data, compute_chi_square, compute_mannwhitneyu, compute_ttest, z_test_for_proportions
from eda import plot_age_distribution, plot_gender_distribution, plot_tenure_distribution, plot_logins, plot_calls

# File paths
file_path_demo = 'Raw/df_final_demo.txt'
file_path_experiment = 'Raw/df_final_experiment_clients.txt'
file_path_combined = 'Raw/df_combined.txt'

# Load data
df_final_demo = load_data(file_path_demo)
df_final_experiment_clients = load_data(file_path_experiment)
df_combined = load_data(file_path_combined)

# Clean data
df_final_demo = clean_data(df_final_demo)
df_final_experiment_clients = clean_data(df_final_experiment_clients)
df_combined = clean_data(df_combined)

# Merge data
Clean_Data = merge_data(df_final_demo, df_final_experiment_clients, df_combined)
Clean_Data.to_csv('Clean_Data.csv', index=False)

# EDA
plot_age_distribution(Clean_Data)
plot_gender_distribution(Clean_Data)
plot_tenure_distribution(Clean_Data)
plot_logins(Clean_Data)
plot_calls(Clean_Data)

# Hypothesis Testing
# Completion Rate
chi2, p_value = compute_chi_square(Clean_Data, 'variation', 'process_step')
print(f"Chi-square test: chi2 = {chi2}, p = {p_value}")

# Dwell Time
control_dwell_time = Clean_Data[Clean_Data['variation'] == 'Control']['dwell_time']
test_dwell_time = Clean_Data[Clean_Data['variation'] == 'Test']['dwell_time']
u_stat, p_value = compute_mannwhitneyu(control_dwell_time, test_dwell_time)
print(f"Mann-Whitney U test: U = {u_stat}, p = {p_value}")

# Error Rates
chi2_errors, p_value_errors = compute_chi_square(Clean_Data, 'variation', 'process_step')
print(f"Error Rates Chi-square test: chi2 = {chi2_errors}, p = {p_value_errors}")

# Completion Rate with Cost-Effectiveness Threshold
control_success = Clean_Data[(Clean_Data['variation'] == 'Control') & (Clean_Data['process_step'] == 'confirm')].shape[0]
control_total = Clean_Data[Clean_Data['variation'] == 'Control'].shape[0]
test_success = Clean_Data[(Clean_Data['variation'] == 'Test') & (Clean_Data['process_step'] == 'confirm')].shape[0]
test_total = Clean_Data[Clean_Data['variation'] == 'Test'].shape[0]
z_score, p_value = z_test_for_proportions(control_success, control_total, test_success, test_total)
print(f"Z-test for proportions: z = {z_score}, p = {p_value}")

# Age Hypothesis Test
control_age = Clean_Data[Clean_Data['variation'] == 'Control']['clnt_age']
test_age = Clean_Data[Clean_Data['variation'] == 'Test']['clnt_age']
t_stat, p_value_age = compute_ttest(control_age, test_age)
print(f"T-test for age: t = {t_stat}, p = {p_value_age}")
