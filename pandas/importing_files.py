"""
CSV = Comma Separeted Values
JSON = JavaScript Object Notation
"""

import pandas as pd

df = pd.read_csv("pandas\data.csv")

print(df)
"""
for printing full data -> 'df.to_string()'
"""
# print(df.to_string())

