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


# salary_data_df.drop(
#     salary_data_df[salary_data_df['CalYear'] != 2022].index, inplace=True)

# print(salary_data_df.tail())


# def agg_salary():
#     salay_calc = salary_data_df.groupby(
#         salary_data_df['Department']).Annual_Rate.agg(['count', 'min', 'max', 'mean', 'sum']).rename(columns={'count': 'Employee_Count', 'min': 'Lowest_Salary', 'max': 'Highest_Salary', 'mean': 'Average_Salary', 'sum': 'Department_Total'})

#     return print(salay_calc)


# agg_salary()


def agg_2022_salary(year):
    filterYear = salary_data_df["CalYear"].isin([year])
    dataByYear = salary_data_df[filterYear]
    salay_calc = dataByYear.groupby(
        dataByYear['Department']).Annual_Rate.agg(['count', 'min', 'max', 'mean', 'sum']).rename(columns={'count': 'Employee_Count', 'min': 'Lowest_Salary', 'max': 'Highest_Salary', 'mean': 'Average_Salary', 'sum': 'Department_Total'})

    return print(salay_calc)


agg_2022_salary(2021)


def max_2021_salary(year):
    salary_data_df['Annual_Rate'] = salary_data_df['Annual_Rate'].astype(
        np.int64)
    filterYear = salary_data_df["CalYear"].isin([year])
    filterRateMax = salary_data_df["Annual_Rate"].max()
    dataByYearAsc = salary_data_df[filterYear]

    dataByYearAsc.sort_values(["Annual_Rate"],
                              axis=0,
                              ascending=[False],
                              inplace=True)

    dataByYearTop = dataByYearAsc[:1]
    return dataByYearTop


print('The highest paid employee of 2022 is: \n',
      max_2021_salary(2018))


# def plot_salary(salary_data_df):
#     test = salary_data_df.groupby(['Department'])
#     test_sal = test['Annual_Rate'].agg(['mean'])
#     return sns.histplot(data=salary_data_df, x=test)


# plot_salary(salary_data_df)


# test = salary_data_df.groupby(['Department'])
# test.aggregate({'Annual_Rate': ['mean'],
#                 'Incentive_Allowance': ['max', 'min'],
#                 'Annual_Rate': ['sum']}).reset_index()
# print(test)
# plt.plot(test, test_sal, 'o')
# plt.figure(figsize=(20, 5))
# plt.hist(test, test_sal)
# plt.xticks(test[::1], rotation="vertical")
# plt.xlabel('Department')
# plt.ylabel('Salary Budget')
# plt.show()
