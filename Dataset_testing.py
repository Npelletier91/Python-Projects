import pandas as pd
import numpy as np

import statsmodels.api as sm
import warnings

import spicy

from scipy.stats import ttest_ind, norm

dataset = pd.read_csv("C:\\Users\\Nicol\\Documents\\GitHub Repos\\Python-Projects\\dataset_1.csv")

num_rows, num_cols = dataset.shape
print(f"Numer of rows:{num_rows}")
print(f"Number of columns:{num_cols}")

summary_stats = dataset.describe()
print("Descriptive Statistics:")
print(summary_stats)

if len(dataset) >= 8:
    prob = norm.cdf(2.5, loc=dataset['column_1'].mean(), scale=dataset['column_1'].std())
    print(f"Probability: {prob}")
else:
    print("Insufficient data for probability calculation.")

warnings.filterwarnings("ignore")
group_a_data = dataset[dataset['group'] == 'A']['column_2']
group_b_data = dataset[dataset['group'] == 'B']['column_2']
group_c_data = dataset[dataset['group'] == 'C']['column_2']
if len(group_a_data) >= 8 and len(group_b_data) >= 8:
    t_stat, p_value = ttest_ind(group_a_data, group_b_data)
    t_statC, p_valueC = ttest_ind(group_a_data, group_c_data)
    t_statB, p_valueB = ttest_ind(group_b_data, group_c_data)
    print(f"T-Statistic comparing group A and B in column 2: {t_stat}")
    print(f"P-Value comparing group A and B in column 2: {p_value}")
    print(f't-stats comparing group A and C in column 2: {t_statC}')
    print(f"P-Value comparing group A and C in column 2: {p_valueC}")
    print(f't-stats comparing group B and C in column 2: {t_statB}')
    print(f"P-Value comparing group B and C in column 2: {p_valueB}")
else:
    print("Insufficient data for hypothesis testing.")
    
numeric_columns = dataset.select_dtypes(include=[np.number]).columns
corr_matrix = dataset[numeric_columns].corr()
print("Correlation Matrix:")
print(corr_matrix)

if len(dataset) >= 8:
    x = dataset[['column_1', 'column_2', 'feature_1', 'feature_2']]
    y = dataset['target']
    x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()
    print(model.summary())
else:
    print("insufficient data for regression analysis.")