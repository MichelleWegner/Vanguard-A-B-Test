# Vanguard A/B Test Project

## Project Description
This project analyzes the impact of a new user interface (UI) on completion rates and user experience at Vanguard. An A/B test was conducted to determine whether the new UI leads to higher completion rates and better user interaction.

## Data Sources
- **Client Profiles (df_final_demo):** Demographic data of the clients.
- **Digital Footprints (df_final_web_data):** Divided into pt_1 and pt_2, these datasets contain the digital traces and activities of the clients.
- **Experiment Roster (df_final_experiment_clients):** List of clients who participated in the experiment.

## Data Cleaning and Preprocessing
- **Handling Missing Values:** Removal of rows with missing values and duplicates.
- **Normalization and Encoding:** Standardizing numerical fields and encoding categorical variables.
- **Merging Datasets:** Combining the various datasets into a consolidated dataset.

## Analysis
1. **Demographic Analysis:** Examination of age distribution, gender distribution, and tenure of clients.
2. **Behavioral Analysis:** Analysis of login frequency and call frequency.
3. **Hypothesis Testing:** Examination of completion rates and time spent on each step.

## Results
- The new user interface led to a significantly higher completion rate.
- Improvements in usability and a reduction in error rates were observed.

## Recommendations

- **Rollout of the New Design:** Implement the new UI across the entire platform.

- **Continuous Optimization:** Utilize user feedback and further A/B tests to continuously improve the design.

- **Targeted Adjustments:** Perform deeper analysis of specific customer segments to identify additional optimization potentials.

- **Enhanced Customer Support:** Consider providing additional training or support options based on the call frequency analysis.

## Usage
- **Main Analysis Notebook:** `Main.ipynb`
- **Required Data:** `Clean_Data.csv`


## Authors

Michelle Wegner & Sulaiman Bah


# Presentation :
https://www.canva.com/design/DAGMsRJKIPM/b2lfiO4DHY2TqfGa_CMQRQ/edit?utm_content=DAGMsRJKIPM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
