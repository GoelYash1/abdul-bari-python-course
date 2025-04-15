import csv
import pprint

f = open('Employees.csv','r')

rdr = csv.DictReader(f) # it is a iterator
employee_dict = {r['Name']:r for r in rdr}

"""
# This will not print anything because r is already read in the employee_dict
for row in rdr:
    print(row)
"""

pprint.pprint(employee_dict)

f.close()