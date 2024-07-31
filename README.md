# Vanguard A/B Test Analysis

### Project Overview

This project is part of the Module 2 curriculum and aims to analyze the results of an A/B test conducted by Vanguard, a US-based investment management company.
The goal of the test was to determine if a new, more intuitive User Interface (UI) with contextual prompts improved the user experience and increased completion rates.

### Data Sources

The analysis uses three main datasets:

Data Sources: URL: https://github.com/data-bootcamp-v4/lessons/tree/main/5_6_eda_inf_stats_tableau/project/files_for_project

Client Profiles (df_final_demo): Contains demographic information such as age, gender, and account details.

Digital Footprints (df_final_web_data): Details of client interactions online, split into two parts.

Experiment Roster (df_final_experiment_clients): Indicates which clients were part of the experiment (Control or Test group).

## Methodology
1. Data Cleaning and Preparation
Merging datasets based on client IDs.
Handling missing values and duplicates.
Ensuring data consistency and integrity.

### 2. Exploratory Data Analysis (EDA)
Analysis of client demographics and behaviors.
Visualization of age distribution, tenure, and activity levels.

### 3. Performance Metrics
Completion Rate: Percentage of users completing the process.
Time Spent on Each Step: Average time spent on each process step.
Error Rates: Number of errors or drop-offs during the process.

### 4. Hypothesis Testing
Completion Rate: Testing if the new UI leads to higher completion rates.
Time Spent: Testing if the new UI reduces time spent on each step.
Error Rates: Testing if the new UI reduces errors.

### 5. Experiment Evaluation
Assessment of the experiment's design, duration, and data quality.

## Key Findings

The new UI significantly increased the completion rate compared to the old UI.

There was no significant difference in time spent on each step between the two groups.

The new UI reduced error rates, indicating an improvement in user experience.

### Tools and Libraries Used

Python: For data processing and analysis.

Pandas: Data manipulation and cleaning.

Seaborn & Matplotlib: Data visualization.

SciPy: Statistical testing.

Tableau: Interactive visualizations.

### How to Run the Project

Clone the repository: git clone <repository_url>

Navigate to the project directory.

Install required libraries: pip install -r requirements.txt

Run the analysis scripts: python main.py

Conclusion
The project successfully demonstrated that the new UI design improved the user experience by increasing the completion rate and reducing errors. The analysis provides valuable insights for Vanguard's future UI/UX design decisions.

Authors
Michelle Wegner & Sulaiman Bah



