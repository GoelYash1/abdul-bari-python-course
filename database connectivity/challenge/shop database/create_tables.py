import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("shop.db")
cursor = conn.cursor()

# Create Customer table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customer (
    CustID TEXT PRIMARY KEY,
    Cname TEXT,
    Address TEXT
)
""")

# Create Product table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Product (
    ProdNo TEXT PRIMARY KEY,
    Pname TEXT,
    Price INTEGER
)
""")

# Create Order table
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

conn.commit()
conn.close()
