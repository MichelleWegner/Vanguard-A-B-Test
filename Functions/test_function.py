# test_functions.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from functions import load_data, combine_data, clean_data, remove_outliers, chi_square_test, mann_whitney_u_test, z_test_proportion

# Sample test to check if the functions are working as expected
file_paths = ['./Clean Data/Clean_Data.csv']
df_list = load_data(file_paths)
df_combined = combine_data(df_list)

clean_df = clean_data(df_combined)
clean_df = remove_outliers(clean_df, 'bal')

print(clean_df.head())
