import sqlite3

class Database:
    def __init__(self, db_name="library.db"):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()
        self.books()

    def books(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS library(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                year INT NOT NULL
            )
    """)
        self.connect.commit()
        
    def add_book(self, title, author, year):
        self.cursor.execute("INSERT INTO library (title, author, year) VALUES (?, ?, ?)", (title, author, year))
        self.connect.commit()

    def find_book_by_title(self, title):
        self.cursor.execute("SELECT * FROM library WHERE title = ?", (title,))
        return self.cursor.fetchone()
    
    def update_book_year(self, title, year):
        self.cursor.execute(f"UPDATE library SET year = ? WHERE title = ?",(year, title))
        return self.connect.commit()
    
    def delete_book_by_title(self, title):
        self.cursor.execute("DELETE FROM library WHERE title = ?", (title,))
        self.connect.commit()
        print(f"Книга {title} удалена")

    def close(self):
        self.connect.close()