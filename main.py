import pandas as pd
import os
import numpy as np

# Create salary data dataframe from the SalaryData excel document.
# https://data.louisvilleky.gov/dataset/employee-salary-data

path = "Users/"

salary_data_df = pd.read_excel(os.path.join(
    path, r'C:\Users\miche\OneDrive\Desktop\Code Louisville\Code_along_project\code_along_proj\data\SalaryData.xlsx'), usecols='A:I')


# Data Clean-up where we remove row where names are missing

salary_data_df['Employee_Name'].replace('', np.nan, inplace=True)
salary_data_df.dropna(subset=['Employee_Name'], inplace=True)

salary_data_df.filter('CalYear')

print()
