"""
Pandas is a powerful open-source Python library used for data manipulation, cleaning, analysis, and preprocessing.

It helps us work with structured data such as:

CSV files
Excel files
SQL databases
JSON files
Tables

In Machine Learning, Pandas is one of the first libraries used because models require clean and organized data.

The name ( PANDAS )comes from:

Pan → Panel (multi-dimensional data)
Das → Data Analysis

So, Pandas = Panel Data Analysis.

"""
import pandas as pd

# print(pd.__version__) 

"""
Pandas has two primary data structures:

1. Series (1D):
A Series is a one-dimensional labeled array.

Example:

Index	Value
0	10
1	20
2	30
3	40

Think of it as a single column in Excel.

2. DataFrame (2D):
A DataFrame is a two-dimensional table with rows and columns.

Example:

Emp_ID	Name	Salary
101	Rahul	50000
102	Amit	60000
103	Priya	70000

Think of it as an Excel sheet.

Pandas Workflow in Machine Learning:

Collect Dataset
        ↓
Load using Pandas
        ↓
Explore Data
        ↓
Clean Data
        ↓
Handle Missing Values
        ↓
Feature Engineering
        ↓
Convert to NumPy
        ↓
Train ML Model

"""


">>> Series"

data = [100,102,104,200,202]
series = pd.Series(data,index=["a","b","c","d","e"])
# custom index
# series = pd.Series(data,index=["apartment #1","apartment #2","apartment #3"])

print(series)
print(series.loc["a"]) #to find specific elem
series.loc["a"] = 99
print(series.loc["a"])

print("Integer base location : ")
print(series.iloc[0])
print(series.iloc[1])
print(series.iloc[2])

# accesing value with condition.
print("Accesing value with condition:")
print(series[series < 200])
print(series[series >= 200])

print("Calories example!")

calories = {"Day 1": 1750,"Day 2": 2100,"Day 3": 1700}
# since our dictionary is key:val so the index will be key we dont need to parse index separately.
series = pd.Series(calories)

print(series.loc["Day 1"])
print(series.loc["Day 2"])
print(f"Day 3 value before changing {series.loc["Day 3"]}")
series.loc["Day 3"] += 500 
print(f"Day 3 value after changing {series.loc["Day 3"]}")

print(series[series >= 2000])
