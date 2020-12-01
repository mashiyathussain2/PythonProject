import datetime

year = int(input("Enter the year:"))
date = datetime.datetime(year,1,1)
day = date.strftime("%A")
print(f"First day of the year {year} is : {day}")
