# storage/sql_storage.py

import sqlite3

class SQLStorage:
    def __init__(self, db_name='r_event.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                body TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS meals (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                meal_name TEXT NOT NULL,
                category TEXT NOT NULL,
                area TEXT NOT NULL,
                instructions TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def insert_post(self, title, body):
        self.cursor.execute('INSERT INTO posts (title, body) VALUES (?, ?)', (title, body))
        self.connection.commit()

    def insert_meal(self, meal_name, category, area, instructions):
        self.cursor.execute('INSERT INTO meals (meal_name, category, area, instructions) VALUES (?, ?, ?, ?)', (meal_name, category, area, instructions))
        self.connection.commit()

    def close(self):
        self.connection.close()
