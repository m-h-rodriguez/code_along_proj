import pandas as pd
import os
import numpy as np

# Create salary data dataframe from the SalaryData excel document.
# https://data.louisvilleky.gov/dataset/employee-salary-data

path = "Users/"

salary_data_df = pd.read_excel(os.path.join(
    path, r'C:\Users\miche\OneDrive\Desktop\Code Louisville\Code_along_project\code_along_proj\data\SalaryData.xlsx'), usecols='A:I')


# Data Clean-up where we remove rows where names are missing/blank

salary_data_df['Employee_Name'].replace('', np.nan, inplace=True)
salary_data_df.dropna(subset=['Employee_Name'], inplace=True)


# Data Analysis

# print the data types of each column in the data set
print(salary_data_df.dtypes)

print(salary_data_df[salary_data_df['A'] >= 2020]
      & (salary_data_df['E'].max()))

# print(salary_data_df[salary_data_df['Annual_Rate'].max()])

# def extract_2020_salary(year):
#     rate_2020 = []
#     for rate in year:
#         if year == 2020:
#             rate_2020.append(rate)
#     return rate_2020
