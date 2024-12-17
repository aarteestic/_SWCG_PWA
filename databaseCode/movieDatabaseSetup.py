import sqlite3

con = sqlite3.connect('SWCG.db')

cur = con.cursor()


cur.execute(''' CREATE TABLE movie(title, year, rating, genre, thumbnail, director, id) ''') #single genre functionality currently
# will accept STRING (NOT list) of available genres:
# SCI-FI, ACTION, COMEDY, ROMANCE, HORROR
#title, year, rate, genres, url, director, id


# GENRES: COMEDY, ROMANCE, DRAMA, ACTION, HISTORY, FANTASY
cur.execute('''
        INSERT INTO movie VALUES
            ('Monty Python and the Holy Grail', 1975, 8.2, 'COMEDY, ROMANCE', 'https://m.media-amazon.com/images/M/MV5BZmQwZWNhYjktNDMzMi00MmNkLWJiMjUtNGI0ZjZlNTk1NzllXkEyXkFqcGc@._V1_.jpg', 'Terry Jones, Terry Gilliam', 1),
            ('The Shawshank Redemption', 1994, 9.3, 'DRAMA', 'https://m.media-amazon.com/images/M/MV5BMDAyY2FhYjctNDc5OS00MDNlLThiMGUtY2UxYWVkNGY2ZjljXkEyXkFqcGc@._V1_FMjpg_UX1000_.jpg', 'Frank Darabont', 2),
            ('The Godfather', 1972, 9.2, 'ACTION, DRAMA', 'https://m.media-amazon.com/images/M/MV5BMTIzMDc4MzA2Ml5BMl5BanBnXkFtZTcwODU0MzA3MQ@@._V1_.jpg', 'Christopher Nolan', 3),
            ('12 Angry Men', 1957, 7.2, 'DRAMA', 'https://m.media-amazon.com/images/M/MV5BMTU4OTg2YmUtY2Y4OC00ZjI3LWE0MDItMjdiZjA0MjE1YThlXkEyXkFqcGc@._V1_.jpg', 'Sidney Lumet', 4),
            ('The Lord of the Rings: The Return of the King', 2003, 5, 'FANTASY', 'https://m.media-amazon.com/images/M/MV5BMzA2ZDNjNDMtM2MwMy00ZWVhLTljYTgtMDI4MDNmN2E5ZDM2XkEyXkFqcGc@._V1_.jpg', 'Peter Jackson', 5),
            ("Schindler's List", 1993,  9.9, 'DRAMA, HISTORY', 'https://m.media-amazon.com/images/M/MV5BNjM1ZDQxYWUtMzQyZS00MTE1LWJmZGYtNGUyNTdlYjM3ZmVmXkEyXkFqcGc@._V1_.jpg', 'Steven Spielberg', 6),
            ("Pulp Fiction", 1994, 8.9, 'DRAMA', 'https://m.media-amazon.com/images/M/MV5BY2UwMTI1MDgtMDIzZC00YTJkLWE1MjMtMjE5NTI3MDU5Njg0XkEyXkFqcGc@._V1_.jpg', 'Quentin Tarantino', 7),
            ("Forrest Gump", 1994, 8.8, 'DRAMA, ROMANCE', 'https://m.media-amazon.com/images/M/MV5BNDYwNzVjMTItZmU5YS00YjQ5LTljYjgtMjY2NDVmYWMyNWFmXkEyXkFqcGc@._V1_.jpg', 'Robert Zemeckis', 8),
            ("The Good, the Bad, and the Ugly", 1966, 8.8, 'DRAMA', 'https://m.media-amazon.com/images/M/MV5BNGE1NTBlNDktZTZjNS00MmJlLTkwYTYtYTZmZTM0NWQ2NDIxXkEyXkFqcGc@._V1_.jpg', 'Sergio Leone', 9),
            ("Fight Club", 1999, 8.8, 'DRAMA', 'https://m.media-amazon.com/images/M/MV5BOTgyOGQ1NDItNGU3Ny00MjU3LTg2YWEtNmEyYjBiMjI1Y2M5XkEyXkFqcGc@._V1_.jpg', 'David Fincher', 10),
            ("Inception", 2010, 8.8, 'ACTION', 'https://m.media-amazon.com/images/M/MV5BMTMyMzYxMDQ3NV5BMl5BanBnXkFtZTcwNTA1NTcwMw@@._V1_.jpg', 'Christopher Nolan', 11),
            ("The Matrix", 1999, 8.7, 'ACTION', 'https://m.media-amazon.com/images/M/MV5BZjVkOGM1ZTctZGZmOC00MTM0LWFjYjctNjg2MTg1YTM4N2VlXkEyXkFqcGc@._V1_.jpg', 'Lana Wachowski, Lilly Wachowski', 12),
            ("GoodFellas", 1990, 8.7, 'DRAMA', 'https://m.media-amazon.com/images/M/MV5BMGMyN2E4OTgtZTg1Zi00ODFhLThhYjctMGRjMmVlYjYzYWI1XkEyXkFqcGc@._V1_.jpg', 'Martin Scorsese', 13),
            ("Interstellar", 2014, 8.7, 'DRAMA', 'https://m.media-amazon.com/images/M/MV5BYzdjMDAxZGItMjI2My00ODA1LTlkNzItOWFjMDU5ZDJlYWY3XkEyXkFqcGc@._V1_.jpg', 'Christopher Nolan', 14),
            ("Seven", 1995, 8.6, 'DRAMA', 'https://m.media-amazon.com/images/M/MV5BY2IzNzMxZjctZjUxZi00YzAxLTk3ZjMtODFjODdhMDU5NDM1XkEyXkFqcGc@._V1_.jpg', 'David Fincher', 15),
            ("It's a Wonderful Life", 1946, 8.6, 'ROMANCE, DRAMA', 'https://m.media-amazon.com/images/M/MV5BMDM4OWFhYjEtNTE5Yy00NjcyLTg5N2UtZDQwNDZlYjlmNDU5XkEyXkFqcGc@._V1_.jpg', 'Frank Capra', 16),
            ("Seven Samurai", 1954, 8.6, 'ACTION, DRAMA', 'https://m.media-amazon.com/images/M/MV5BZjliMWExOTMtZDQ3ZS00NWU3LWIyN2EtMjllNzk3ZTNlYzg4XkEyXkFqcGc@._V1_.jpg', 'Akira Kurosawa', 17),
            ("The Silence of the Lambs", 1991, 8.6, 'DRAMA', 'https://m.media-amazon.com/images/M/MV5BNDdhOGJhYzctYzYwZC00YmI2LWI0MjctYjg4ODdlMDExYjBlXkEyXkFqcGc@._V1_.jpg', 'Jonathan Demme', 18),
            ("Saving Private Ryan", 1998, 8.6, 'DRAMA', 'https://m.media-amazon.com/images/M/MV5BZGZhZGQ1ZWUtZTZjYS00MDJhLWFkYjctN2ZlYjE5NWYwZDM2XkEyXkFqcGc@._V1_.jpg', 'Steven Spielberg', 19),
            ("City of God", 2002, 8.6, 'DRAMA', 'https://m.media-amazon.com/images/M/MV5BYWJhZjVmN2QtMzdmMi00ZThjLThkODEtOTkwNGI4ZmNkOWVkXkEyXkFqcGc@._V1_.jpg', 'Fernando Meirelles, Katia Lund', 20),
            ("The Green Mile", 1999, 8.6, 'DRAMA', 'https://m.media-amazon.com/images/M/MV5BNTEyY2E4OGItZGE4Yy00OTI1LThmMWMtNDIyMmY3YzU0MGY0XkEyXkFqcGc@._V1_.jpg', 'Frank Darabont', 21),
            ("Life Is Beautiful", 1997, 8.6, 'COMEDY, DRAMA, ROMANCE', 'https://m.media-amazon.com/images/M/MV5BYmZhNTZmMTEtMjQ4OC00MmRkLTkzYjItNmVjZWFjNjdlYjNkXkEyXkFqcGc@._V1_.jpg', 'Roberto Benigni', 22),
            ("Terminator 2: Judgement Day", 1991, 8.6, 'ACTION', 'https://m.media-amazon.com/images/M/MV5BNGMyMGNkMDUtMjc2Ni00NWFlLTgyODEtZTY2MzBiZTg0OWZiXkEyXkFqcGc@._V1_.jpg', 'James Cameron', 23),
            ("Star Wars: Episode IV - A New Hope", 1977, 8.7, 'ACTION, FANTASY', 'https://m.media-amazon.com/images/M/MV5BOGUwMDk0Y2MtNjBlNi00NmRiLTk2MWYtMGMyMDlhYmI4ZDBjXkEyXkFqcGc@._V1_.jpg', 'George Lucas', 24),
            ("Back to the Future", 1985, 8.5, 'COMEDY', 'https://m.media-amazon.com/images/M/MV5BZmM3ZjE0NzctNjBiOC00MDZmLTgzMTUtNGVlOWFlOTNiZDJiXkEyXkFqcGc@._V1_.jpg', 'Robert Zemeckis', 25) 
                    ''')

con.commit()

cur.close()
con.close()


