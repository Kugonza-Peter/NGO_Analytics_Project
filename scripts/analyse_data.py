import pandas as pd

data = pd.read_csv("data/beneficiaries_cleaned.csv")

print("DATASET SUMMARY")
print("----------------")

print("Total beneficiaries:", len(data))
print("Average age:", round(data["age"].mean(), 2))
print("Total amount received:", data["amount_received"].sum())
print("Average attendance rate:", round(data["attendance_rate"].mean(), 2))

print("\nBENEFICIARIES BY DISTRICT")
print(data["district"].value_counts())

print("\nBENEFICIARIES BY PROGRAM")
print(data["program"].value_counts())

print("\nBENEFICIARIES BY GENDER")
print(data["gender"].value_counts())