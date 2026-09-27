import pandas as pd

data = pd.read_csv("data/beneficiaries_cleaned.csv")

program_summary = data.groupby("program").agg(
    beneficiaries=("beneficiary_id", "count"),
    total_amount=("amount_received", "sum"),
    average_age=("age", "mean"),
    average_attendance=("attendance_rate", "mean")
).reset_index()

program_summary["average_age"] = program_summary["average_age"].round(2)
program_summary["average_attendance"] = program_summary["average_attendance"].round(2)

program_summary.to_csv("data/program_summary.csv", index=False)

print("Program summary created successfully!")
print(program_summary)