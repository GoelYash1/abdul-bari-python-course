class Employee:
    employee_count = 101
    def __init__(self,  name, salary, designation):
        self.emp_id = 'e' + str(Employee.employee_count)
        self.name = name
        self.salary = salary
        self.designation = designation
        Employee.employee_count+=1

    def show_details(self):
        print(f"Employee Id: {self.emp_id}")
        print(f"Name: {self.name}")
        print(f"Salary: {self.salary}")
        print(f"Designation: {self.designation}")

    @classmethod
    def total_emp(cls):
        return cls.employee_count - 101

e1 = Employee('Yash', 750000, 'Senior Analyst')
e2 = Employee('Nitin',750000, 'Senior Analyst')

print("Employee 1 details:")
e1.show_details()
print("\nEmployee 2 details:")
e2.show_details()

print(f"Total Employees: {Employee.total_emp()}")