import sys
from PyQt6.QtWidgets import QApplication,QMainWindow
from PyQt6.QtCore import Qt
from PyQt6 import uic
from MySQLdb import _mysql
from models.Book import Book
from models.Author import Author
from controllers.books import BookController
from controllers.authors import AuthorController
from controllers.reads import ReadController


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # Load GUI
        uic.loadUi('views/main.ui', self)
        # Attach Methods to Buttons
        self.tableBooks.cellPressed.connect(self.onItemClickBooks)
        self.tableAuthors.cellPressed.connect(self.onItemClickAuthors)
        self.getBookFormBtn.clicked.connect(self.open_new_book_window)
        self.getAuthorFormBtn.clicked.connect(self.open_new_author_window)
        # Connecto the Database
        self.connect_to_db()
        # load db into books/authors tables & most recent Book into the display window
        self.update_books_table()
        self.update_authors_table()
        self.onItemClickBooks(-1)


    def connect_to_db(self):
        try:
            self.db = _mysql.connect('localhost','root','root','pyqt_books')
            print('Beep Boop, DB is up...')
        except Exception as e:
            print('Bop Boop Beep, something went wrong. so very wrong...')



    def onItemClickBooks(self, row):
        data = 'DETAILS:\n'
        data += f'{BookController.onItemClickBooks(self,row)}\n'
        data += ReadController.fetch_reads(self,'book',self.all_books[row].id)
        self.instanceDisplay.setText(data)
    def onItemClickAuthors(self, row):
        AuthorController.onItemClickAuthors(self,row)

    def update_books_table(self):
        BookController.update_books_table(self)
    def update_authors_table(self):
        AuthorController.update_authors_table(self)

    def open_new_book_window(self):
        BookController.open_new_book_window(self)
    def open_new_author_window(self):
        AuthorController.open_new_author_window(self)

    def create_new_book(self):
        BookController.create_new_book(self)
    def create_new_author(self):
        AuthorController.create_new_author(self)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = MainWindow()
    main.show()

try: sys.exit(app.exec())
except: print('Goodbye Bop Boop Bing...')