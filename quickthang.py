import sqlite3


con = sqlite3.connect('SWCG.db')
cur = con.cursor()

cur.EXECUTE(''' ALTER TABLE movie ADD image TEXT ''')
con.commit()

cur.close()
con.close()