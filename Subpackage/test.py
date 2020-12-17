import sqlite3
conn=sqlite3.connect('HMS.db')
c=conn.cursor()
c.execute("SELECT * FROM patients")
print(c.fetchall())
conn.commit()
conn.close()