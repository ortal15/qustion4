def create_table():
    """פונקציה ליצירת טבלת הסרטים ובנוסף להכנסת המידע שלהם"""
    import os
    import sqlite3

    if os.path.exists("part_c_def.db"):
        os.remove("part_c_def.db")
    else:
        print("The file does not exist")
    conn = sqlite3.connect('part_c_def.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    movie_name TEXT NOT NULL UNIQUE, -- Unique movie name
    genre TEXT NOT NULL,
    country TEXT NOT NULL,
    language TEXT NOT NULL,
    year INTEGER NOT NULL CHECK (year >= 2009), -- Ensures movie is from the last 15 years
    revenue REAL NOT NULL CHECK (revenue >= 0) -- Revenue in millions, cannot be negative
    );''')
    cursor.execute('''INSERT INTO movies (movie_name, genre, country, language, year, revenue) VALUES
    ('Oppenheimer', 'Biography', 'USA', 'English', 2023, 960),
    ('Barbie', 'Comedy', 'USA', 'English', 2023, 1440),
    ('Dune Part Two', 'Sci-Fi', 'USA', 'English', 2024, 700),
    ('John Wick 4', 'Action', 'USA', 'English', 2023, 440),
    ('Everything Everywhere All at Once', 'Sci-Fi', 'USA', 'English', 2022, 140),
    ('The Batman', 'Action', 'USA', 'English', 2022, 772),
    ('Spider Man No Way Home', 'Action', 'USA', 'English', 2021, 1920),
    ('Top Gun Maverick', 'Action', 'USA', 'English', 2022, 1490),
    ('The Whale', 'Drama', 'USA', 'English', 2022, 55),
    ('Guardians of the Galaxy Vol 3', 'Action', 'USA', 'English', 2023, 845),
    ('Parasite', 'Thriller', 'South Korea', 'Korean', 2019, 266),
    ('Train to Busan 2', 'Horror', 'South Korea', 'Korean', 2020, 92),
    ('Decision to Leave', 'Mystery', 'South Korea', 'Korean', 2022, 23),
    ('Joker', 'Drama', 'USA', 'English', 2019, 1074),
    ('Tenet', 'Sci-Fi', 'USA', 'English', 2020, 365),
    ('The Irishman', 'Crime', 'USA', 'English', 2019, 8),
    ('Ford v Ferrari', 'Drama', 'USA', 'English', 2019, 225),
    ('1917', 'War', 'UK', 'English', 2019, 385),
    ('The Farewell', 'Drama', 'USA', 'English/Chinese', 2019, 23),
    ('The Banshees of Inisherin', 'Comedy', 'Ireland', 'English', 2022, 49),
    ('Django Unchained', 'Western', 'USA', 'English', 2012, 426),
    ('Avengers Endgame', 'Action', 'USA', 'English', 2019, 2798),
    ('Black Panther', 'Action', 'USA', 'English', 2018, 1347),
    ('Coco', 'Animation', 'USA', 'English/Spanish', 2017, 807),
    ('Mad Max Fury Road', 'Action', 'Australia', 'English', 2015, 380),
    ('Inception', 'Sci-Fi', 'USA', 'English', 2010, 837),
    ('The Revenant', 'Adventure', 'USA', 'English', 2015, 532),
    ('La La Land', 'Musical', 'USA', 'English', 2016, 447),
    ('The Secret in Their Eyes', 'Crime', 'Argentina', 'Spanish', 2009, 34),
    ('No Time to Die', 'Action', 'UK', 'English', 2021, 774);''')
    conn.commit()
    conn.close()


def c_question():
    """קוד בפייטון הקולט מהמשתמש פרטי סרט ואז מבצע שאילתת INSERT להוספת הסרט
לטבלת הסרטים"""
    import sqlite3

    conn = sqlite3.connect('part_c_def.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    movie_id: int = int(input('Please insert the id of the movie:'))
    movie_name: str = input('Please insert the movie name:')
    genre: str = input('Please insert the movie genre:')
    country: str = input('Please insert the movie country:')
    language: str = input('Please insert the movie language:')
    year: int = int(input('Please insert the movie year:'))
    revenue: float = float(input('Please insert the movie revenue:'))
    cursor.execute('''INSERT INTO movies
    VALUES (?,?,?,?,?,?,?)''', (movie_id, movie_name, genre, country, language, year, revenue))

    conn.commit()
