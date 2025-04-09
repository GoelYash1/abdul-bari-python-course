import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect('univ.db')
cursor = conn.cursor()

# Create the Students table
cursor.execute('''
CREATE TABLE IF NOT EXISTS student (
    Roll INTEGER PRIMARY KEY,
    Name TEXT,
    City TEXT,
    Deptno INTEGER
)
''')

# Insert data
students_data = [
    (1, 'Ajay', 'Delhi', 10),
    (2, 'Vijay', 'Kolkata', 10),
    (3, 'Ajay', 'Mumbai', 20),
    (4, 'Ramesh', 'Delhi', 30),
    (5, 'Suneeta', 'Lucknow', 40),
    (6, 'Anita', 'Kolkata', 30),
    (7, 'Raj', 'Jaipur', 30),
    (8, 'Ali', 'Lucknow', 40),
    (9, 'Michael', 'Cochin', 10),
    (10, 'Pavan', 'Vijaywada', 20),
    (11, 'Suraj', 'Hyderabad', 10),
    (12, 'Altaf', 'Bangaluru', 40),
    (13, 'Ravi', 'Indore', 20),
    (14, 'Verma', 'Delhi', 20),
    (15, 'Sharma', 'Vizag', 10),
]

cursor.executemany('INSERT INTO student (Roll, Name, City, Deptno) VALUES (?, ?, ?, ?)', students_data)

# Commit and close
conn.commit()
conn.close()
