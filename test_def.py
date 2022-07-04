from audioop import avg
import babel.numbers
import pandas as pd
import os
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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

# print(salary_data_df.tail())


def avg_salary(df):
    avg_salary = salary_data_df.groupby('Department', as_index=False)[
        'Annual_Rate'].mean()
    dept_count = salary_data_df[['Department']
                                ].value_counts().reset_index(name='counts')
    #dept = salary_data_df['Department'].unique()
    return avg_salary, dept_count


print(avg_salary(salary_data_df))


# plt.plot(dept, salary, 'o')
# plt.figure(figsize=(20, 5))
# plt.scatter(dept, salary)
# plt.xticks(dept[::1], rotation="vertical")
# plt.xlabel('Department')
# plt.ylabel('Salary Budget')
# plt.show()
