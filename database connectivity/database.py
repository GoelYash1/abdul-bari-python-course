import sqlite3

conn = sqlite3.connect('univ.db')
cur = conn.cursor()

# Create dept table
cur.execute('CREATE TABLE dept(deptno INTEGER PRIMARY KEY, name TEXT)')
conn.commit()

# Create student table with foreign key referencing dept table
cur.execute('''
    CREATE TABLE student(
        roll INTEGER PRIMARY KEY,
        name TEXT,
        city TEXT,
        deptno INTEGER,
        FOREIGN KEY(deptno) REFERENCES dept(deptno)
    )
''')
conn.commit()

cur.close()
conn.close()
