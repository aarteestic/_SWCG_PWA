import sqlite3

con = sqlite3.connect('SWCG.db')

cur = con.cursor()


cur.execute(''' CREATE TABLE movie(title, year, rating, genre, thumbnail) ''') #single genre functionality currently
# may add genre as list later, but for now it will accept string of available genres:
# SCI-FI, ACTION, COMEDY, ROMANCE, HORROR

cur.execute('''
        INSERT INTO movie VALUES
            ('Monty Python and the Holy Grail', 1975, 8.2, 'COMEDY', 'https://m.media-amazon.com/images/M/MV5BZmQwZWNhYjktNDMzMi00MmNkLWJiMjUtNGI0ZjZlNTk1NzllXkEyXkFqcGc@._V1_.jpg'),
            ('And Now for Something Completely Different', 1971, 7.5, 'ROMANCE', 'https://resizing.flixster.com/lq_ckOf77SBBIwKES92ImXjDpew=/fit-in/352x330/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p629_i_v9_ac.jpg'),
            ('Super Secret Spicy Movie', 2035, 1.9, 'HORROR', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOPprZxGfjH1s5qFWLK5P1zsmi1PJvurGedw&s')
        ''')

con.commit()



#TABLE movie takes values -- title, year, score.


res = cur.execute("SELECT genre FROM movie") #gives tuple of 3 values of movie names

movieTable = cur.execute('''SELECT name FROM sqlite_master WHERE type='table' AND name='movie' ''').fetchone()
# checks if table exists
print(res.fetchall())