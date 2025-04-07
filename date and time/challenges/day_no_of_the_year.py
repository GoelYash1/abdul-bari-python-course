import datetime

str_date = input("Enter a date(dd-mm-yyyy): ")
d,m,y = str_date.split("-")

dt = datetime.date(int(y),int(m),int(d))
dt_b = datetime.date(int(y), 1,1)

dt_d = dt - dt_b

print(dt_d.days + 1)
