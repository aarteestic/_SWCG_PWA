import sqlite3

con = sqlite3.connect('SWCG.db')

cur = con.cursor()


cur.execute(''' CREATE TABLE movie(title, year, rating, genre) ''') #single genre functionality currently
# may add genre as list later, but for now it will accept string of available genres:
# SCI-FI, ACTION, COMEDY, ROMANCE, HORROR

cur.execute('''
        INSERT INTO movie VALUES
            ('Monty Python and the Holy Grail', 1975, 8.2, 'COMEDY'),
            ('And Now for Something Completely Different', 1971, 7.5, 'ROMANCE'),
            ('Super Secret Spicy Movie', 2035, 1.9, 'HORROR')
        ''')

con.commit()



#TABLE movie takes values -- title, year, score.


res = cur.execute("SELECT title FROM movie") #gives tuple of 3 values of movie names

movieTable = cur.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='movie' ''').fetchone()
# checks if table exists
listOfNames = res.fetchall()