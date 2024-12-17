import sqlite3

con = sqlite3.connect('SWCG.db')

cur = con.cursor()


cur.execute(''' CREATE TABLE movie(title, year, rating, genre, thumbnail, director, id) ''') #single genre functionality currently
# will accept STRING (NOT list) of available genres:
# SCI-FI, ACTION, COMEDY, ROMANCE, HORROR
#title, year, rate, genres, url, director, id


# GENRES: COMEDY, ROMANCE, DRAMA, ACTION
cur.execute('''
        INSERT INTO movie VALUES
            ('Monty Python and the Holy Grail', 1975, 8.2, 'COMEDY, ROMANCE', 'https://m.media-amazon.com/images/M/MV5BZmQwZWNhYjktNDMzMi00MmNkLWJiMjUtNGI0ZjZlNTk1NzllXkEyXkFqcGc@._V1_.jpg', 'Terry Jones, Terry Gilliam', 1),
            ('The Shawshank Redemption', 1994, 9.3, 'DRAMA', 'https://m.media-amazon.com/images/M/MV5BMDAyY2FhYjctNDc5OS00MDNlLThiMGUtY2UxYWVkNGY2ZjljXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg', 'Frank Darabont', 2),
            ('The Godfather', 1972, 9.2, 'ACTION, DRAMA', 'https://m.media-amazon.com/images/M/MV5BMTIzMDc4MzA2Ml5BMl5BanBnXkFtZTcwODU0MzA3MQ@@._V1_.jpg', 'Christopher Nolan', 3),
            ('12 Angry Men', 1957, 7.2, 'DRAMA', 'https://m.media-amazon.com/images/M/MV5BMTU4OTg2YmUtY2Y4OC00ZjI3LWE0MDItMjdiZjA0MjE1YThlXkEyXkFqcGc@._V1_.jpg', 'Sidney Lumet', 4),
            ('The Lord of the Rings: The Return of the King', 2003, 5, 'FANTASY', 'https://m.media-amazon.com/images/M/MV5BMzA2ZDNjNDMtM2MwMy00ZWVhLTljYTgtMDI4MDNmN2E5ZDM2XkEyXkFqcGc@._V1_.jpg', 'Peter Jackson', 5),
            ("Schindler's List", 1993,  9.9, 'DRAMA, HISTORY', 'https://m.media-amazon.com/images/M/MV5BNjM1ZDQxYWUtMzQyZS00MTE1LWJmZGYtNGUyNTdlYjM3ZmVmXkEyXkFqcGc@._V1_.jpg', 'Steven Spielberg', 6)
                    ''')

con.commit()

cur.close()
con.close()


