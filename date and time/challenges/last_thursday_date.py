import datetime
THURSDAY_IDX = 3

str_date = input("Enter a date(DD:MM:YYYY): ")
d,m,y = str_date.split(":")

dt = datetime.date(day=int(d),month=int(m),year=int(y))
dt_day = dt.weekday()

last_thursday_date = None
if dt_day > THURSDAY_IDX:
    last_thursday_date = dt - datetime.timedelta(dt.weekday() - THURSDAY_IDX)
else:
    last_thursday_date = dt - datetime.timedelta(7 - (THURSDAY_IDX - dt.weekday()))

print(last_thursday_date, last_thursday_date.weekday())