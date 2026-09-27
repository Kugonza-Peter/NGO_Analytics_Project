import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data/beneficiaries_cleaned.csv")

# Average attendance by district
district_attendance = data.groupby("district")["attendance_rate"].mean()

district_attendance.plot(kind="bar")
plt.title("Average Attendance by District")
plt.xlabel("District")
plt.ylabel("Average Attendance Rate")
plt.tight_layout()

plt.savefig("reports/attendance_by_district.png")

print("District attendance chart created successfully!")