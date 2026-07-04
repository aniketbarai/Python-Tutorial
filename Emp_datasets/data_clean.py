import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("Emp_datasets/employees.csv")

print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

# Convert numeric columns
df["Salary(INR)"] = pd.to_numeric(df["Salary(INR)"], errors="coerce")
df["Performance Rating"] = pd.to_numeric(df["Performance Rating"], errors="coerce")

# Replace inf values
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Fill missing values
df["Salary(INR)"].fillna(df["Salary(INR)"].mean(), inplace=True)
df["Performance Rating"].fillna(df["Performance Rating"].median(), inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

# Replace negative salaries
df["Salary(INR)"] = np.where(
    df["Salary(INR)"] < 0,
    df["Salary(INR)"].mean(),
    df["Salary(INR)"]
)

# Remove salary outliers using 3-sigma rule
salary_mean = df["Salary(INR)"].mean()
salary_std = df["Salary(INR)"].std()

lower_bound = salary_mean - 3 * salary_std
upper_bound = salary_mean + 3 * salary_std

df = df[
    (df["Salary(INR)"] >= lower_bound) &
    (df["Salary(INR)"] <= upper_bound)
]

# Save cleaned dataset
df.to_csv("cleaned_emp_data.csv", index=False)

print("\nData Cleaning Completed!")