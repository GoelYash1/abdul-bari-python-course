import sqlite3

conn = sqlite3.connect('univ.db')

cur = conn.cursor()

# cur.execute('update dept set name="Chem" where name="Mech"')
# rows = cur.execute('select * from dept')

cur.execute('delete from dept where deptno=40')
conn.commit()

# print(rows.fetchall())
cur.close()
conn.close()