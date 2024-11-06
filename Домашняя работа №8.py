import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_name="notes.db"):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()
        self.notes_table()

    def notes_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS notes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                created_at TIMESTAMP
            )
    """)
        self.connect.commit()

    def add_note(self, title, content, created_at):
        self.cursor.execute("INSERT INTO notes (title, content, created_at) VALUES (?, ?, ?)", (title, content, created_at))
        self.connect.commit()

    def all_note(self):
        self.cursor.execute(" SELECT * FROM notes ")
        return self.cursor.fetchall()
        
    
    def update_note(self, id, title, content):
        self.cursor.execute(f"UPDATE notes SET (title, content) = (?, ?) WHERE id = ?",(title, content, id))
        return self.connect.commit()
    
    def delete_note(self, id):
        self.cursor.execute("DELETE FROM notes WHERE id = ?", (id,))
        self.connect.commit()
        print(f"Заметка удалена")

    def get_note(self, id):
        self.cursor.execute("SELECT * FROM notes WHERE id = ?", (id,))
        return self.cursor.fetchone()

    def add(self):
        title = input("Заголовок: ")
        content = input("Содержание: ")
        created_at = f"{datetime.now():%d.%m.%Y %H:%M}"
        self.add_note(title, content, created_at)
        print("Заметка добавлена")

    def all(self):
        for i in self.all_note():
            print(f"""id - {i[0]}
Заголовок:
{i[1]}
Содержание:
{i[2]}
Создано в {i[3]}\n""")
                
    def update(self):
        id = int(input("Введите id: "))
        if self.get_note(id):
            title = input("Введите новый заголовок: ")
            content = input("Введите новое содержание: ")
            self.update_note(id, title, content)
            print("Заметка редактирована")
        else:
            print("Заметка не найдено")

    def delete(self):
        id = input("Введите id для удаления заметки: ")
        if self.get_note(id):
            self.delete_note(id)
        else:
            print("Книга не найдена")

def markdown():
    database = Database()
    while True:
        print("""
1. Добавить заметку
2. Посмотреть все заметки
3. Редактировать заметку
4. Удалить заметку
5. Выйти""")
        action = int(input("Выберите действие: "))
        if action == 1:
            database.add()
        elif action == 2:
            database.all()
        elif action == 3:
            database.update()
        elif action == 4:
            database.delete()
        elif action == 5:
            return False
        else:
            print("Пожалуйста выберите одну из номеров действий")

markdown()