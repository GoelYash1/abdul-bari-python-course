work_hours = [int(hr) for hr in input("Enter weekly work hours separated by space: ").split()]
hourly_sal = int(input("Enter hourly Salary: "))
total_hrs_worked = sum(work_hours)
total_salary = total_hrs_worked * hourly_sal

print(total_salary)


