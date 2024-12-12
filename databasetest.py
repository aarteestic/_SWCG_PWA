import sqlite3

con = sqlite3.connect('SWCG.db')

cur = con.cursor()
cur.execute('''
        INSERT INTO movie VALUES
            ('Monty Python and the Holy Grail', 1975, 8.2),
            ('And Now for Something Completely Different', 1971, 7.5),
            ('Super Secret Spicy Movie', 2035, 1.9)
        ''')

con.commit()



#TABLE movie takes values -- title, year, score.


res = cur.execute("SELECT title FROM movie") #gives tuple of 3 values of movie names

movieTable = cur.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='movie' ''').fetchone()
# checks if table exists
listOfNames = res.fetchall()