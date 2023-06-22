from PyQt6.QtWidgets import QMainWindow,QTableWidgetItem
from PyQt6 import uic
from models.Book import Book

class BookController():

    # GUI CONTROLS
    def onItemClickBooks(self, row):
        self.labelDisplay.setText(f'Showing Details About Book {self.all_books[row].title}')
        return  self.all_books[row].display_full_data()

    def open_new_book_window(self):
        newBookWindow = QMainWindow()
        form = uic.loadUi('views/bookForm.ui')
        for author in self.all_authors:
            form.inputAuthor.addItem(f'{author.return_full_name()} | ID:{author.id.decode("utf-8")}')
        form.createBookBtn.clicked.connect(self.create_new_book)
        newBookWindow.setCentralWidget(form)
        self.newBookWindow = newBookWindow
        self.newBookWindow.show()


    #  CREATE
    def create_new_book(self):
        form = self.newBookWindow.centralWidget()
        new_book = {
            'author_id': int(form.inputAuthor.currentText().split(':')[1]),
            'title': form.inputTitle.text(),
            'pages': int(form.inputPages.text())
        }
        Book.create_new_book(self.db, new_book)
        self.update_authors_table()
        self.update_books_table()
        self.onItemClickBooks(-1)
        self.newBookWindow.close()

    # READ
    def update_books_table(self):
        self.all_books = Book.fecth_all_books(self.db)
        self.tableBooks.setRowCount(len(self.all_books))
        row = 0
        for book in self.all_books:
            self.tableBooks.setItem(row,0,QTableWidgetItem(book.title))
            self.tableBooks.setItem(row,1,QTableWidgetItem(f"{book.author.return_full_name()}"))
            self.tableBooks.setItem(row,2,QTableWidgetItem(book.pages))
            row += 1