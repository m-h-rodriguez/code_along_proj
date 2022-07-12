
import matplotlib.pyplot as plt
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
salary_data_df['Annual_Rate'] = salary_data_df['Annual_Rate'].astype(np.int64)


# tech_emp = salary_data_df.loc[salary_data_df['Department']
#                               == 'Technology Services']

salary = salary_data_df.groupby(['CalYear'])['Annual_Rate'].sum()


def tech_emp(year):
    filterYear = salary_data_df["CalYear"].isin([year])
    test = salary_data_df[filterYear].loc[salary_data_df['Department']
                                          == 'Technology Services']
    return test


print(tech_emp(2022).nlargest(5, "Annual_Rate"))


plt.bar(tech_emp(2021), salary)
plt.title('Louisville Metro Incentive Budget By Year')
plt.xlabel('Year')
plt.ylabel('Incentive Budget')
plt.gca().set_yticklabels(['${:,.0f}'.format(x)
                           for x in plt.gca().get_yticks()])
plt.show()
