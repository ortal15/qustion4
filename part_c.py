from part_c_def import create_table, c_question

create_table()

import sqlite3

conn = sqlite3.connect('part_c_def.db')
conn.row_factory = sqlite3.Row
cursor = conn.cursor()

"""א. כתוב קוד בפייטון המציג את כל הסרטים"""
cursor.execute('''SELECT movie_name FROM movies''')
rows = cursor.fetchall()
for row in rows:
    print(dict(row))

"""ב. כתוב קוד בפייטון הקולט מהמשתמש שם או חלק מ - שם של סרט ומחזיר את כל הסרטים
אשר מכילים את אותו השם , רמז: LIKE
לדוגמא אם נקלט השם “batman “יוצג הסרט – “batman the“"""

user_movie = input("Enter name or part of a movie name: ")

cursor.execute("SELECT * FROM movies WHERE movie_name LIKE ?", ('%' + user_movie + '%',))
rows = cursor.fetchall()

if rows is None:
    print("The name is not found in the movie database.")
else:
    for row in rows:
        print(dict(row))

"""ג. כתוב קוד בפייטון הקולט מהמשתמש פרטי סרט ואז מבצע שאילתת INSERT להוספת הסרט
לטבלת הסרטים"""

c_question()
cursor.execute('''SELECT * FROM movies''')
rows = cursor.fetchall()
for row in rows:
    print(dict(row))
