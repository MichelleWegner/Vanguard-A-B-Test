
# test_eda.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import pandas as pd
import eda

# Load cleaned data
clean_df = pd.read_csv('Clean Data/Clean_Data.csv')

# Perform EDA
eda.plot_age_distribution(clean_df)
eda.plot_gender_distribution(clean_df)
eda.plot_tenure_distribution(clean_df)
eda.plot_login_frequency(clean_df)
eda.plot_call_frequency(clean_df)
