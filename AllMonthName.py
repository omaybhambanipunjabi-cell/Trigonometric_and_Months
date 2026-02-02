import calendar
import datetime
print(" Months using calendar module")
for i in range(1, 13):
    print(f"Month {i}: {calendar.month_name}")

print("\n" + "-"*30 + "\n")

print("Months using daetime module ")
for i in range(1, 13):
    obj_date = datetime.date(2000, i, 1)

    print(f"Month {i}: {obj_date.strftime}")