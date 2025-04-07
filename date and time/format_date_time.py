from datetime import *
from time import strptime

"""
    # strftime() - datetime to string
    # strptime() - string to datetime
"""

dt1 = datetime(2010, 1, 1, 10, 20, 30)
dt1_str = f"{dt1.day} {dt1.strftime('%b, %a %y. %H:%M:%S')}"

dt2 = '07 April, 2025. 01:10:10'
dt2_obj = strptime(dt2, '%d %B, %Y. %H:%M:%S')

print(dt1_str, dt2_obj)





