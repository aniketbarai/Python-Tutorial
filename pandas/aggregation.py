import pandas as pd

"""
Aggregate functions = Reduces a set of values into a single summary value Used to summarize and analyze the data.

"""
df = pd.read_csv("pandas\data.csv")

# Whole DataFrame 

# print(df.mean(numeric_only=True))
# print(df.sum(numeric_only=True))
# print(df.min(numeric_only=True))
# print(df.max(numeric_only=True))
# print(df.median(numeric_only=True))
# print(df.count())

#Single Column

# print(df["Height"].mean())
# print(df["Height"].min())
# print(df["Height"].max())
# print(df["Height"].count())

group = df.groupby("Type1")
# print(group["Height"].mean())
grp = df.groupby("Legendary")
print(grp["Height"].mean())
print(grp["Height"].max())
print(grp["Height"].min())
print(grp["Height"].sum())
print(grp["Height"].count())
