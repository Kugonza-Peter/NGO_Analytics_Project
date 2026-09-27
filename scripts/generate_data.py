import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

names = [
    "John", "Mary", "David", "Sarah", "Peter",
    "Grace", "James", "Annet", "Robert", "Joy",
    "Isaac", "Esther", "Michael", "Rebecca", "Daniel"
]

districts = ["Wakiso", "Kampala", "Mukono", "Jinja", "Mbarara"]
genders = ["Male", "Female"]
programs = ["Youth Skills", "Agriculture", "Health", "Education"]

data = []

start_date = datetime(2025, 1, 1)

for i in range(1, 501):
    name = random.choice(names) + " " + random.choice(
        ["Mugisha", "Namukasa", "Okello", "Achieng", "Kato"]
    )

    registration_date = start_date + timedelta(
        days=random.randint(0, 364)
    )

    data.append({
        "beneficiary_id": f"B{i:04d}",
        "name": name,
        "gender": random.choice(genders),
        "age": random.randint(18, 60),
        "district": random.choice(districts),
        "program": random.choice(programs),
        "registration_date": registration_date.strftime("%Y-%m-%d"),
        "attendance_rate": random.randint(50, 100),
        "amount_received": random.randint(100000, 1000000)
    })

df = pd.DataFrame(data)

df.to_csv("data/beneficiaries_large.csv", index=False)

print("Dataset created successfully!")
print("Number of records:", len(df))