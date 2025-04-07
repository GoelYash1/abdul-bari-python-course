import datetime

str_date = input("Enter a date(DD-MM-YYYY): ")
d,m,y = str_date.split("-")

try:
    d1 = datetime.date(int(y),int(m),int(d))
except ValueError:
    print("Some Error")
