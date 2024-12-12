import sqlite3

con = sqlite3.connect('SWCG.db')
cur = con.cursor()

res = cur.execute("SELECT name FROM user").fetchall()


print(res)

for i in range(0, len(res)):
    print(res[i][0])
