import csv

covid_dict = [
    {'Country': 'India', 'Doses': '186Cr', 'People': '84.1Cr', 'Percentage': 61},
    {'Country': 'China', 'Doses': '330Cr', 'People': '84.1Cr', 'Percentage': 88.1},
    {'Country': 'United States', 'Doses': '56.8Cr', 'People': '21.9Cr', 'Percentage': 66.4},
    {'Country': 'Brazil', 'Doses': '42.4Cr', 'People': '16.2Cr', 'Percentage': 76.4},
    {'Country': 'Indonesia', 'Doses': '39Cr', 'People': '16.2Cr', 'Percentage': 59.3}
]

with open('CSVDict.csv','w',newline='') as f:
    wrtr = csv.DictWriter(f,['Country','Doses','People','Percentage'])
    wrtr.writeheader()
    for d in covid_dict:
        wrtr.writerow(d)