import pandas as pd
import os
import numpy as np

# filtered values used to extract the max and min salary are setting a value on a copy of a slice from the dataframe.
# To ignore this warning as a means of only pulling the values, the chained mode assignment sets this to none for it to ignore the warning
pd.options.mode.chained_assignment = None

# function borrowed to print out banners/headers in order to separate different parts of the project for visibility


def banner(message, banner="-"):

    line = banner * 11
    print(f"\n{line}")
    print(message)
    print(line)

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
#####
banner("Information About the Data Set")
#####
print(salary_data_df.dtypes)


# display all available Departments in the data set and print them on new lines
dept = list(salary_data_df['Department'].unique())
print('These are the departments listed for the metro salary analysis: ', *dept, sep='\n')


#####
banner("Employee Information")
#####


def agg_salary(year):
    filterYear = salary_data_df["CalYear"].isin([year])
    dataByYear = salary_data_df[filterYear]
    salay_calc = dataByYear.groupby(
        dataByYear['Department']).Annual_Rate.agg(['count', 'min', 'max', 'mean', 'sum']).rename(columns={'count': 'Employee_Count', 'min': 'Lowest_Salary', 'max': 'Highest_Salary', 'mean': 'Average_Salary', 'sum': 'Department_Total'})

    return print(salay_calc)


agg_salary(2018)


def max_salary(year):
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


print('The highest paid employee of the selected year is: \n',
      max_salary(2016))


def min_salary(year):
    salary_data_df['Annual_Rate'] = salary_data_df['Annual_Rate'].astype(
        np.int64)
    filterYear = salary_data_df["CalYear"].isin([year])
    filterRateMax = salary_data_df["Annual_Rate"].min()
    dataByYearDesc = salary_data_df[filterYear]

    dataByYearDesc.sort_values(["Annual_Rate"],
                               axis=0,
                               ascending=[True],
                               inplace=True)

    dataByYearBotton = dataByYearDesc[:1]
    return dataByYearBotton


print('The lowest paid employee of the selected year is: \n',
      min_salary(2019))


# salary_2022 = []

# for index, rows in salary_data_df.iterrows():
#     salary_list = [rows.CalYear, rows.Employee_Name,
#                    rows.Department, int(rows.Annual_Rate)]

#     if rows.CalYear == 2022:
#         salary_2022.append(salary_list)


# print(salary_2022)
