import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customer (
    CustID TEXT PRIMARY KEY,
    Cname TEXT,
    Address TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Product (
    ProdNo TEXT PRIMARY KEY,
    Pname TEXT,
    Price INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders (
    OrderNo TEXT,
    CustID TEXT,
    ProdNo TEXT,
    Qty INTEGER,
    FOREIGN KEY (CustID) REFERENCES Customer(CustID),
    FOREIGN KEY (ProdNo) REFERENCES Product(ProdNo)
)
""")

# Insert data into Customer table
customers = [
    ('C101', 'Anita', 'Delhi'),
    ('C102', 'Raj', 'Hyderabad'),
    ('C103', 'Michael', 'Kolkata'),
    ('C107', 'Ali', 'Delhi'),
    ('C109', 'Sharma', 'Chennai'),
]
cursor.executemany("INSERT INTO Customer VALUES (?, ?, ?)", customers)

# Insert data into Product table
products = [
    ('P10', 'Toothpaste', 20),
    ('P11', 'Toothbrush', 10),
    ('P12', 'Lotion', 30),
    ('P13', 'Shampoo', 25),
    ('P14', 'Soap', 10),
]
cursor.executemany("INSERT INTO Product VALUES (?, ?, ?)", products)

# Insert data into Orders table
orders = [
    ('10005', 'C101', 'P10', 1),
    ('10005', 'C101', 'P11', 2),
    ('12389', 'C109', 'P12', 1),
    ('12389', 'C109', 'P14', 1),
    ('12389', 'C109', 'P11', 2),
    ('63017', 'C103', 'P13', 4),
    ('63017', 'C103', 'P10', 1),
    ('63017', 'C103', 'P11', 4),
    ('71222', 'C101', 'P12', 2),
    ('71222', 'C101', 'P13', 1),
    ('96351', 'C102', 'P14', 1),
]
cursor.executemany("INSERT INTO Orders VALUES (?, ?, ?, ?)", orders)

# Commit and close
conn.commit()
conn.close()
