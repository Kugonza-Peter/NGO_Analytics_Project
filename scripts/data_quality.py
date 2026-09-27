import pandas as pd

data = pd.read_csv("data/beneficiaries_cleaned.csv")

print("DATA QUALITY REPORT")
print("-------------------")

print("Rows:", len(data))
print("Columns:", len(data.columns))

print("\nMissing values:")
print(data.isnull().sum())

print("\nDuplicate rows:", data.duplicated().sum())

print("\nData types:")
print(data.dtypes)