"""
>>> DataFrame (2D):
A DataFrame is a two-dimensional table with rows and columns.

Example:

Emp_ID	 Name	 Salary
101	     Rahul	 50000
102	     Amit	  60000
103	     Priya	 70000

Think of it as an Excel sheet.
"""

import pandas as pd

data = {"Name":["Spongebob","Modric","Messi","Ronaldo"],
        "Age":[30,38,39,48],
}

df = pd.DataFrame(data,index=["Player 1","Player 2","Player 3","Player 4"])
# .DataFrame() --> is a constructor
print(df)
# df.loc["..."] --> loc = location by label
print(df.loc["Player 4"])
print(df.loc["Player 2"])
print(df.iloc[1])

# Add a new column
df["Position"] = ["Goalkeeper","N/A","Forward","Striker"]
print(df)

# Add a new row
new_row = pd.DataFrame([
    {"Name":"Neymar","Age":32,"Position":"Attacker"},
    {"Name":"Mbappe","Age":31,"Position":"Neutral"}],index=["Player 5","Player 6"])
df = pd.concat([df,new_row])
print(df)



