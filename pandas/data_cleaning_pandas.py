import pandas as pd

"""
============================================================
                DATA CLEANING IN PANDAS
============================================================

Definition:
-----------
Data Cleaning is the process of detecting, correcting,
or removing incorrect, incomplete, duplicate,
irrelevant, or inconsistent data from a dataset.

In Data Science and Machine Learning,
almost 70-80% of the work is spent cleaning data.

Why is Data Cleaning Important?
-------------------------------
✔ Improves model accuracy
✔ Removes incorrect information
✔ Prevents errors during analysis
✔ Makes visualization meaningful
✔ Produces reliable business insights

Common Data Cleaning Tasks
--------------------------
1. Remove unnecessary columns
2. Handle missing values
3. Fix inconsistent values
4. Standardize text
5. Correct data types
6. Remove duplicate records
7. Handle outliers
8. Rename columns
9. Trim unwanted spaces
10. Convert date/time formats

------------------------------------------------------------
Load Dataset
------------------------------------------------------------
"""

df = pd.read_csv("pandas/data.csv")

print("Original Shape:", df.shape)

"""
============================================================
1. DROP IRRELEVANT COLUMNS
============================================================

Sometimes datasets contain columns that are not useful
for analysis or Machine Learning.

Syntax:
-------
df.drop(columns=[...])

Parameters:
-----------
columns -> list of column names

axis=1 also represents columns.

Example:
--------
"""

# df = df.drop(columns=["Legendary", "No"])

"""
Before
------
No | Name | Type1 | Legendary

After
-----
Name | Type1

Advantages
----------
✔ Reduces memory usage
✔ Makes dataset cleaner
✔ Removes unnecessary features

Interview Question
------------------
Q. Difference between dropping rows and columns?

Rows    -> axis=0 (default)
Columns -> axis=1
"""



"""
============================================================
2. HANDLE MISSING VALUES
============================================================

Missing values are represented as:
----------------------------------
NaN
None
Blank cells

Very Important Functions
------------------------
dropna()
fillna()
isnull()
notnull()

------------------------------------------------------------
A) Remove rows containing missing values
------------------------------------------------------------
"""

# df = df.dropna()

"""
Drop rows where Type2 is missing
"""

# df = df.dropna(subset=["Type2"])

"""
------------------------------------------------------------
B) Replace missing values
------------------------------------------------------------
"""

# Replace only one column
df = df.fillna({"Type2": "None"})

"""
You can also replace numeric values.

Example:

df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

Common Strategies
-----------------

Numeric Columns
---------------
Mean
Median
Mode

Categorical Columns
-------------------
Mode
Unknown
None
Other

Interview Tip
-------------
Never blindly remove rows.
If too many rows are removed,
valuable information may be lost.
"""



"""
============================================================
3. FIX INCONSISTENT VALUES
============================================================

Sometimes same value is written differently.

Example
-------
Grass
GRASS
grass
Grass

These represent the same category.

replace() helps fix them.

Syntax
------
replace({old:new})

Example
-------
"""

# df["Type1"] = df["Type1"].replace({
#     "Grass": "GRASS",
#     "Fire": "FIRE",
#     "Water": "WATER"
# })

"""
Other Examples
--------------
Male, male, M
Female, female, F

Should be standardized into one format.
"""



"""
============================================================
4. STANDARDIZE TEXT
============================================================

Text data should follow one consistent format.

Useful String Methods
---------------------

str.lower()
str.upper()
str.title()
str.strip()
str.replace()

Examples
--------
"""

# Convert everything to lowercase
# df["Name"] = df["Name"].str.lower()

# Convert everything to uppercase
# df["Name"] = df["Name"].str.upper()

# First letter capital
# df["Name"] = df["Name"].str.title()

# Remove extra spaces
# df["Name"] = df["Name"].str.strip()

"""
Example

Before
------
 Pikachu
PIKACHU
pikachu

After
-----
pikachu
"""



"""
============================================================
5. FIX DATA TYPES
============================================================

Wrong datatype is one of the most common issues
in real-world datasets.

Check data types

df.dtypes

Convert datatype

astype()

Example
-------
"""

df["Legendary"] = df["Legendary"].astype(bool)

"""
Other Examples
--------------

df["Age"] = df["Age"].astype(int)

df["Salary"] = df["Salary"].astype(float)

df["Name"] = df["Name"].astype(str)

Why?
----
Correct datatypes
✔ Faster computation
✔ Less memory
✔ Easier calculations
✔ Required for ML algorithms
"""



"""
============================================================
6. REMOVE DUPLICATES
============================================================

Duplicate rows can occur because of:
------------------------------------
• Data entry mistakes
• Multiple imports
• Merging datasets

Check duplicates

df.duplicated()

Remove duplicates

drop_duplicates()

Example
-------
"""

df = df.drop_duplicates()

"""
You can also remove duplicates based on selected columns.

Example

df.drop_duplicates(subset=["Name"])

Keep only first occurrence

keep="first"

Keep last occurrence

keep="last"

Remove ALL duplicates

keep=False
"""



"""
============================================================
USEFUL DATA CLEANING FUNCTIONS
============================================================

df.info()
----------------
Quick summary

df.describe()
----------------
Statistics

df.head()
----------------
First 5 rows

df.tail()
----------------
Last 5 rows

df.shape
----------------
(rows, columns)

df.columns
----------------
Column names

df.dtypes
----------------
Data types

df.isnull().sum()
----------------
Missing values count

df.value_counts()
----------------
Frequency of values
"""



"""
============================================================
REAL ML DATA CLEANING PIPELINE
============================================================

Load Dataset
      ↓
Inspect Data
      ↓
Check Missing Values
      ↓
Handle Missing Values
      ↓
Remove Duplicates
      ↓
Fix Datatypes
      ↓
Standardize Text
      ↓
Fix Inconsistent Values
      ↓
Handle Outliers
      ↓
Feature Engineering
      ↓
Ready for ML

Remember:
---------
Garbage In = Garbage Out (GIGO)

No matter how powerful the ML model is,
poor-quality data always leads to poor results.
"""

print("\nFinal Shape:", df.shape)

print("\nData Types")
print(df.dtypes)

print("\nMissing Values")
print(df.isnull().sum())

print("\nFinal Dataset")
print(df.to_string())