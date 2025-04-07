import datetime
from calendar import *

year = int(input("Enter a year: "))

monday = 0
for month in range(1,13):
    dt = datetime.date(year, month, 1)
    if dt.weekday() == 0:
        monday+=1
        print(month,end="   ")

print("\nMonths starting from monday:",monday)