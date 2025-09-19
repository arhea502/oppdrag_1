from datetime import datetime
from dateutil.relativedelta import relativedelta

d1 = datetime(2025, 8, 27)

date_str = input("Enter a date (YYYY-MM-DD): ")

try:
    d2 = datetime.strptime(date_str, "%Y-%m-%d")
except ValueError:
    print("Invalid date format. Please use YYYY-MM-DD.")
    exit()

diff = relativedelta(d1, d2)

print(f"Years: {diff.years}")
print(f"Months: {diff.months}")
print(f"Days: {diff.days}")
