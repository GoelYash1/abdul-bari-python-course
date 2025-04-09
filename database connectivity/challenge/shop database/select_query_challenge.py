import sqlite3

conn = sqlite3.connect('shop.db')

cur = conn.cursor()

# Select all customers
all_customers = cur.execute('SELECT * FROM Customer')
print(all_customers.fetchall())

# Select all customers from Delhi
delhi_customers = cur.execute('SELECT * FROM Customer WHERE address = "Delhi"')
print(delhi_customers.fetchall())

# Select all products with price greater than 20
products_20 = cur.execute('SELECT * FROM Product WHERE price > 20')
print(products_20.fetchall())

# Select names of the products starting with s
products_s = cur.execute('SELECT pname FROM Product WHERE pname like "s%"')
print(products_s.fetchall())

delhi_chennai_customers = cur.execute('SELECT * FROM Customer WHERE address in ("Delhi","Chennai")')
print(delhi_chennai_customers.fetchall())

# Select order no and product no with quantity greater than 1
orders_quantity_greater_1 = cur.execute('SELECT orderno, prodno FROM orders WHERE qty>1')
print(orders_quantity_greater_1.fetchall())

# Name of the customer with order number 10005
cust_name_orderid = cur.execute('SELECT DISTINCT(c.cname) FROM customer c JOIN orders o ON c.custid = o.custid WHERE o.orderno = 10005')
print(cust_name_orderid.fetchall())

cur.close()
conn.close()