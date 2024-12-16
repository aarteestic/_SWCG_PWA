import sqlite3

con = sqlite3.connect('SWCG.db')

cur = con.cursor()


cur.execute(''' CREATE TABLE movie(title, year, rating, genre, thumbnail, director, id) ''') #single genre functionality currently
# will accept STRING (NOT list) of available genres:
# SCI-FI, ACTION, COMEDY, ROMANCE, HORROR

cur.execute('''
        INSERT INTO movie VALUES
            ('Monty Python and the Holy Grail', 1975, 8.2, 'COMEDY, ROMANCE', 'https://m.media-amazon.com/images/M/MV5BZmQwZWNhYjktNDMzMi00MmNkLWJiMjUtNGI0ZjZlNTk1NzllXkEyXkFqcGc@._V1_.jpg', 'Terry Jones, Terry Gilliam', 1),
            ('And Now for Something Completely Different', 1971, 7.5, 'ROMANCE', 'https://resizing.flixster.com/lq_ckOf77SBBIwKES92ImXjDpew=/fit-in/352x330/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p629_i_v9_ac.jpg', 'Wilson', 2),
            ('Super Secret Spicy Movie', 2035, 1.9, 'HORROR', 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOPprZxGfjH1s5qFWLK5P1zsmi1PJvurGedw&s', 'Wilson', 3)
        ''')

con.commit()

cur.close()
con.close()


