import numpy as np
import pandas as pd

salary_df = pd.read_csv(
    "C:\\Users\\miche\\OneDrive\\Desktop\\Code Louisville\\Code_along_project\\code_along_proj\\SalaryData.csv", encoding='unicode_escape')
print(salary_df.head())

print(salary_df.shape)
print(type(salary_df.shape))

n, num_columns = salary_df.shape
print('This is the number of rows: ', n)
print('This is the number of columns: ', num_columns)

dept = list(salary_df['Department'].unique())
print('These are the departments listed for the metro salary analysis: ', *dept, sep='\n')
print('The a department in this list is: ', dept.pop())

print('The 4th department is: ', dept.pop(4))

print('The first 4 departments are: ', dept[0: 4])

print('The hightest salary paid to a metro employee is ',
      salary_df['Annual_Rate'].max())
