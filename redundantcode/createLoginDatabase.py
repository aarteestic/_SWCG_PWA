import sqlite3
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"A secret message")
f.decrypt(token)


print(token)
print(f.decrypt(token))
# example encryption code



con = sqlite3.connect('SWCG.db')

cur = con.cursor()


userTable = cur.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='user' ''').fetchone()
# checks if table exists
if userTable is None:
    cur.execute("CREATE TABLE user(name, password)")
    cur.execute('''
            INSERT INTO user VALUES
                ('Wilson', 'redcodsnapper')
            ''')
    con.commit()
else:
    print('table exists!')

res = cur.execute('''SELECT name FROM user ''').fetchall()
print(res)
