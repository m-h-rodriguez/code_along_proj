from audioop import avg
import babel.numbers
import pandas as pd
import os
import numpy as np
import seaborn as sns

# filtered values used to extract the max and min salary are setting a value on a copy of a slice from the dataframe.
# To ignore this warning as a means of only pulling the values, the chained mode assignment sets this to none for it to ignore the warning
pd.options.mode.chained_assignment = None

path = "Users/"

salary_data_df = pd.read_excel(os.path.join(
    path, r'C:\Users\miche\OneDrive\Desktop\Code Louisville\Code_along_project\code_along_proj\data\SalaryData.xlsx'), usecols='A:I')

salary_data_df['Employee_Name'].replace('', np.nan, inplace=True)
salary_data_df.dropna(subset=['Employee_Name'], inplace=True)

salary_data_df.drop(
    salary_data_df[salary_data_df['CalYear'] != 2022].index, inplace=True)

# print(salary_data_df.head())


def calc_salary(salary_data_df):
    avg_salary = salary_data_df.groupby('Department', as_index=False)[
        'Annual_Rate'].mean()
    dept = salary_data_df['Department'].unique()
    return sns.histplot(data=avg_salary, x=dept, y=avg_salary)


print(calc_salary(salary_data_df))
