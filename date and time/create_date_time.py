import datetime
import time

dt1 = datetime.datetime(2010,1,1,10,10,10)
dt2 = datetime.datetime(month=1,day = 1,year=2011,hour = 10,minute=10,second=10)

print(dt1, dt2)

dat1 = datetime.date(2025, 4, 7)
tim1 = datetime.time(12,51,20)

dt3 = datetime.datetime.combine(dat1,tim1)
print(dt3)

time_now = datetime.datetime.now()
time_today = datetime.datetime.today()
time_epoch_now = time.localtime(time.time())
time_ctime_now_str = time.ctime()

print(f"Time Now: {time_now}")
print(f"Time Today: {time_today}")
print(f"Time Epoch Now: {time_epoch_now}")
print(f"Time Ctime in String: {time_ctime_now_str}")