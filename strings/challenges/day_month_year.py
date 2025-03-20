date_s = input("Enter a date in (dd/mm/yy): ")
date_list = date_s.split("/")

date_day = date_list[0]
date_month = date_list[1]
date_year = date_list[2]

print(
    f'''day: {date_day}
month: {date_month}
year: {date_year}'''
)