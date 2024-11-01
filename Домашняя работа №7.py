from database import Database

class BookService:
    def __init__(self, db_name="library.db"):
        self.db = Database(db_name)

    def add_book(self):
        title = input("Название книги: ")
        if self.db.find_book_by_title(title):
            print("Книга с таким названием уже существует")
            return
        author = input("Автор: ")
        year = int(input("Год выпуска: "))
        self.db.add_book(title, author, year)
        print("Добавлена книга")

    def book_search(self):
        title = input("Введите название книги: ")
        book_data = self.db.find_book_by_title(title)
        if book_data:
            print(f"id - {book_data[0]}\ntitle - {book_data[1]}\nauthor - {book_data[2]}\nyear - {book_data[3]}")
        else:
            print("Не найдено")

    def update_year(self):
        title = input("Введите название книги: ")
        if self.db.find_book_by_title(title):
            year = int(input("Введите год: "))
            self.db.update_book_year(title, year)
            print("Год обновлён")
        else:
            print("Книга не найдена")

    def delete_book(self):
        title = input("Какую книгу вы хотите удалить?: ")
        if self.db.find_book_by_title(title):
            self.db.delete_book_by_title(title)
        else:
            print("Книга не найдена")


def Menu():
    bookService = BookService()
    while True:

        print("""
1. Добавлять книгу.
2. Искать книгу по названию.
3. Обновлять год издания книги.
4. Удалять книгу по названию.
5. Выходить из программы.
""")

        category = int(input("Выберите категорию: "))
        if category == 1:
            bookService.add_book()
        elif category == 2:
            bookService.book_search()
        elif category == 3:
            bookService.update_year()
        elif category == 4:
            bookService.delete_book()
        elif category == 5:
            return False
        else:
            print("Неправильная категория")

Menu()