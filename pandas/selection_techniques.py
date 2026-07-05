import pandas as pd

df = pd.read_csv("pandas\data.csv", index_col="Name")

print(df)

#  SELECTION BY COLUMN

# print(df["Name"])
# print(df["Height"].to_string())
# print(df["Weight"].to_string())

#  SELECTION BY Multiple Column
# print(df[["Name","Height","Weight"]].to_string())

# SELECTION BY ROW/S

# print(df.loc[0])
# print(df.loc[1])
"""
 > index_col="Name" < : This means we are setting our idx as name value. so now we will find location using name.
"""
print(df.loc["Pikachu"])
"""
:  this term is used below which means the data between from charizard <-> blastoise

"""
print(df.loc["Charizard":"Blastoise",["Height","Weight"]])
"""
The below line of code is means:
-rows
0:11 --> range(excluded)
x:x:2 --> steps

-cols
0:3 --> 3 cols only
"""
# print(df.iloc[0:11:2 ,0:3])


pokemon = input("Enter a Pokemon name: ").capitalize()

try:
    print(df.loc[pokemon])
except KeyError:
    print(f"{pokemon} not found!")


