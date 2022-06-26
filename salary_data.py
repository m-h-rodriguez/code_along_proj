# Notes as I worked through the data1_project using the Metro Gov Salary Data
# <Week>.<ModuleNumber>


# Borrowed Function to print the empty line, then a message in a banner

import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def banner(message, banner="-"):

    line = banner * 11
    print(f"\n{line}")
    print(message)
    print(line)

##
# Week 3 Data Structures
##


#####
banner("Content for 3.1")
#####

headers = ["CalYear", "Employee_Name", "Department", "jobTitle", "Annual_Rate",
           "Regular_Rate", "Overtime_Rate", "Incentive_Allowance", "Other", "YTD_Total"]
print(headers)

#####
banner("Content for 3.2")
#####

print(headers[1:3])

#####
banner("Content for 3.3")
#####

text = ['Employee', 'Pay', 'Position', 'Other', 'Department', 'Year']
num = [1, 22, 14, 13, 12, 11, 10, 9]

print('Slicing a list from the 0 index to 3rd index', text[0:3])
print('Now it is time to slice the numbers', num[0:3])

#####
banner("Content for 3.4")
#####

data = {
    "Employee": "Michelle Rodriguez",
    "Position": "Systems Analyst",
    "Employer": "Appriss Insights",

}

print(data["Employee"])

#####
banner("Content for 3.5")
#####

print(type(data))
print(type(data['Position']))
print(type(1))


#####
banner("Content for 4")
#####

# Import pandas module and set it as pd when reading my csv for salary_df

salary_df = pd.read_csv(
    "C:\\Users\\miche\\OneDrive\\Desktop\\Code Louisville\\Code_along_project\\code_along_proj\\SalaryData.csv", encoding='unicode_escape')


#####
banner("Content for 5.1")
#####

print(salary_df.head())

print(salary_df.shape)
print(type(salary_df.shape))

n, num_columns = salary_df.shape
print('This is the number of rows: ', n)
print('This is the number of columns: ', num_columns)

#####
banner("Content for 5.2")
#####

dept = list(salary_df['Department'].unique())
print('These are the departments listed for the metro salary analysis: ', *dept, sep='\n')

# POP removes and returns the last value from the List or the given index value
print(dept.pop())

print(dept.pop(4))

print(dept[0: 4])

dept.append('PTO')
dept[-1]


# converting the 'CalYear' column from string to datetime

salary_df["CalYear"] = salary_df["CalYear"].astype('datetime64[ns]')


def selected_year_salary(year):
    return salary_df["CalYear"].datetime


#####
banner("Content for 6")
#####


def year(salary): return salary_df['CalYear']


year(2020)

print(year(2020))


def salary_by_year(year, departments):
    return salary_df['CalYear'], salary_df["Department"]


print(salary_by_year(2020, 'Parks & Recreation'))


# print(dept_pay_budget)


print('The hightest salary paid to a metro employee is ',
      salary_df['Annual_Rate'].max())


#####
banner("Content for 7")
#####

print(salary_df.sort_values(by='CalYear' and 'Department', ascending=True))

print(salary_df.groupby(['CalYear', 'Department'])['Annual_Rate'].sum())

print(salary_df.groupby(['Employee_Name', 'Department', 'Annual_Rate']))

####
banner("Matplotlib Visualization Demo")
####

print(salary_df.dtypes)

# filterRate = data["Annual_Rate"].isin([])
filterYear = salary_df["CalYear"].isin(["2022"])
salary_df[filterYear]

# plt.figure(figsize=(12, 6))
# plt.scatter(salary_df.groupby('Department'), salary_df.groupby('CalYear'))
# plt.xlabel('Department')
# plt.ylabel('CalYear')
# plt.title('Scatterplot of range of salaries per Department')
# plt.show()
