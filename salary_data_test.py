# Notes as I worked through the data1_project using the Metro Gov Salary Data
# <Week>.<ModuleNumber>


# Borrowed Function to print the empty line, then a message in a banner

import datetime
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
pd.options.mode.chained_assignment = None


def banner(message, banner="-"):

    line = banner * 11
    print(f"\n{line}")
    print(message)
    print(line)

# Import pandas module and set it as pd when reading my csv for salary_df


salary_df = pd.read_csv(
    "C:\\Users\\miche\\OneDrive\\Desktop\\Code Louisville\\Code_along_project\\code_along_proj\\SalaryData.csv", encoding='unicode_escape')

# filterRate = data["Annual_Rate"].isin([])
# filterYear = salary_df["CalYear"].isin(["2022"])
# salary_df[filterYear]


data = pd.read_csv("SalaryData.csv", encoding='unicode_escape')
data['Annual_Rate'] = data['Annual_Rate'].astype(np.int64)
filterYear = data["CalYear"].isin([2022])
filterRate = data["Annual_Rate"].max()
dataByYear = data[filterYear]

dataByYear.sort_values(["Annual_Rate"],
                       axis=0,
                       ascending=[False],
                       inplace=True)

dataByYearTop = dataByYear[:1]

print(dataByYearTop)
