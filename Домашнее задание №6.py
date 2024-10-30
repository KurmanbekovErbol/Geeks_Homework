import sqlite3
from datetime import datetime

connect = sqlite3.connect("Управление_задачами.db")
cursor = connect.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Управление_задачами(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        status TEXT NOT NULL,
        date DATE
    )
""")

def register():
    description = input("Введите новую задачу: ")
    status = input("Вы выполнили эту задачу? (ответьте да или нет): ")
    if status == "да":
        status = "завершена"
    elif status == "нет":
        status = "выполняется"
    date = f"{datetime.now():%d.%m.%Y %H:%M}"

    cursor.execute(""" INSERT INTO Управление_задачами
                   (description, status, date)
                   VALUES (?, ?, ?)""", (description, status, date))
    connect.commit()

def update():
    id = int(input("Укажите id задачу, которую вы хотите обновить: "))
    update = input("Вы выполнили эту задачу? (ответьте да или нет): ")
    if update == "да":
        update = "завершена"
    else:
        update = "выполняется"
    cursor.execute(f"UPDATE Управление_задачами SET status = '{update}' WHERE id = {id}")
    connect.commit()

def delete_tasks():
    id = int(input("Укажите id задачу, которую вы хотите удалить: "))
    cursor.execute(f"DELETE FROM Управление_задачами WHERE id = {id}")
    connect.commit()

def all_tasks():
    cursor.execute(" SELECT * FROM Управление_задачами ORDER BY date")
    tasks = cursor.fetchall()
    for i in tasks:
        print(i)

def running():
    cursor.execute("SELECT * FROM Управление_задачами WHERE status LIKE '%выполняется'")
    runnings = cursor.fetchall()
    for i in runnings:
        print(i)

def completed():
    cursor.execute("SELECT * FROM Управление_задачами WHERE status LIKE '%завершена'")
    completeds = cursor.fetchall()
    for i in completeds:
        print(i)

"Добавление новой задачи."
# register()

"Обновление статуса задачи." 
# update()

"Удаление задачи по её ID." 
# delete_tasks()

"Просмотр всех задач с сортировкой по дате создания."
# all_tasks()

"Поиска задач по статусу"

"Поиск невыполненых задач"
# running()

"Поиск выполненых задач"
# completed()