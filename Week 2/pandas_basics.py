# Pandas Basics Practice

import pandas as pd


data = {
    "Defect": ["Crack", "Scratch", "No Defect"],
    "Count": [5, 8, 2]
}


df = pd.DataFrame(data)

print("DataFrame:")
print(df)


print("\nFirst rows:")
print(df.head())


print("\nStatistics:")
print(df.describe())


df["Checked"] = True

print("\nUpdated Data:")
print(df)
