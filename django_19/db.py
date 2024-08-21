import sqlite3

connection = sqlite3.connect("database.db")
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users
id INTEGER PRIMARY KEY, 
username TEXT NOT NULL,
age INTEGER,
balance INTEGER
)
''')
connection.commit()
connection.close()