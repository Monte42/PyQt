import sys
from PyQt6.QtWidgets import QApplication,QMainWindow,QTableWidgetItem
from PyQt6.QtCore import Qt
from PyQt6 import uic
from MySQLdb import _mysql
from models.Book import Book
from models.Author import Author

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('views/main.ui', self)

        self.tableBooks.cellPressed.connect(self.onItemClickBooks)
        self.tableAuthors.cellPressed.connect(self.onItemClickAuthors)
        self.getBookFormBtn.clicked.connect(self.open_new_book_window)

        self.connect_to_db()

        self.update_books_table()
        self.update_authors_table()




    def connect_to_db(self):
        try:
            self.db = _mysql.connect('localhost','root','root','pyqt_books')
            print('Beep Boop, DB is up...')
        except Exception as e:
            print('Bop Boop Beep, something went wrong. so very wrong...')

    def onItemClickBooks(self, row, col):
        self.labelDisplay.setText(f'Showing Details About Book {self.all_books[row].title}')
        self.instanceDisplay.setText(self.all_books[row].display_full_data())
    def onItemClickAuthors(self, row, col):
        self.labelDisplay.setText(f'Showing Details About Author {self.all_authors[row].return_full_name()}')
        self.instanceDisplay.setText(self.all_authors[row].display_full_data())




    def update_books_table(self):
        self.all_books = Book.fecth_all_books(self.db)
        self.tableBooks.setRowCount(len(self.all_books))
        row = 0
        for book in self.all_books:
            self.tableBooks.setItem(row,0,QTableWidgetItem(book.title))
            self.tableBooks.setItem(row,1,QTableWidgetItem(f"{book.author.return_full_name()}"))
            self.tableBooks.setItem(row,2,QTableWidgetItem(book.pages))
            row += 1

    def update_authors_table(self):
        self.all_authors = Author.fecth_all_authors(self.db)
        self.tableAuthors.setRowCount(len(self.all_authors))
        row = 0
        for author in self.all_authors:
            self.tableAuthors.setItem(row,0,QTableWidgetItem(author.first_name.decode('utf-8')))
            self.tableAuthors.setItem(row,1,QTableWidgetItem(author.last_name.decode('utf-8')))
            self.tableAuthors.setItem(row,2,QTableWidgetItem(f'{len(author.books)}'))
            row += 1



    def open_new_book_window(self):
        newBookWindow = QMainWindow()
        form = uic.loadUi('views/bookForm.ui')
        for author in self.all_authors:
            form.inputAuthor.addItem(f'{author.return_full_name()} | ID:{author.id.decode("utf-8")}')
        form.createBookBtn.clicked.connect(self.create_new_book)
        newBookWindow.setCentralWidget(form)
        self.newBookWindow = newBookWindow
        self.newBookWindow.show()

    def create_new_book(self):
        pass








if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = MainWindow()
    main.show()

try: sys.exit(app.exec())
except: print('Goodbye Bop Boop Bing...')