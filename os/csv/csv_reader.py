import csv

f = open('Employees.csv','r')

csv_reader = csv.reader(f)
next(csv_reader)
for row in csv_reader:
    print(int(row[2]))

f.close()