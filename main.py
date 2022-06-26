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
banner("Data Types in the Salary data set")
#####
print(salary_data_df.dtypes)


#####
banner("Employee Information")
#####
salary_data_df['Annual_Rate'] = salary_data_df['Annual_Rate'].astype(np.int64)
filterYear = salary_data_df["CalYear"].isin([2022])
filterRateMax = salary_data_df["Annual_Rate"].max()
dataByYear = salary_data_df[filterYear]

dataByYear.sort_values(["Annual_Rate"],
                       axis=0,
                       ascending=[False],
                       inplace=True)

dataByYearTop = dataByYear[:1]

print('The highest paid employee of 2022 is: \n', dataByYearTop)

filterRateMin = salary_data_df["Annual_Rate"].min()
dataByYear = salary_data_df[filterYear]

dataByYear.sort_values(["Annual_Rate"],
                       axis=0,
                       ascending=[True],
                       inplace=True)

dataByYearTop = dataByYear[:1]

print('The lowest paid employee of 2022 is: \n', dataByYearTop)


# salary_2022 = []

# for index, rows in salary_data_df.iterrows():
#     salary_list = [rows.CalYear, rows.Employee_Name,
#                    rows.jobTitle, int(rows.Annual_Rate)]

#     if rows.CalYear == 2022:
#         salary_2022.append(salary_list)


# print(salary_2022)


# max_pay_employee = max(salary_2022, key=lambda x: float(x))

# print(str(max_pay_employee))
