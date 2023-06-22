from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem
from PyQt6 import uic
from models.Author import Author


class AuthorController():

    # GUI CONTROLS
    def onItemClickAuthors(self, row):
        self.labelDisplay.setText(f'Showing Details About Author {self.all_authors[row].return_full_name()}')
        self.instanceDisplay.setText(self.all_authors[row].display_full_data())

    def open_new_author_window(self):
        newAuthorWindow = QMainWindow()
        form = uic.loadUi('views/authorForm.ui')
        form.createAuthorBtn.clicked.connect(self.create_new_author)
        newAuthorWindow.setCentralWidget(form)
        self.newAuthorWindow = newAuthorWindow
        self.newAuthorWindow.show()


    # CREATE
    def create_new_author(self):
        form = self.newAuthorWindow.centralWidget()
        new_author = {
            'first_name': form.inputFirstName.text(),
            'last_name': form.inputLastName.text()
        }
        Author.create_new_author(self.db, new_author)
        self.update_authors_table()
        self.update_books_table()
        self.onItemClickAuthors(-1)
        self.newAuthorWindow.close()

    # READ
    def update_authors_table(self):
        self.all_authors = Author.fecth_all_authors(self.db)
        self.tableAuthors.setRowCount(len(self.all_authors))
        row = 0
        for author in self.all_authors:
            self.tableAuthors.setItem(row,0,QTableWidgetItem(author.first_name.decode('utf-8')))
            self.tableAuthors.setItem(row,1,QTableWidgetItem(author.last_name.decode('utf-8')))
            self.tableAuthors.setItem(row,2,QTableWidgetItem(f'{len(author.books)}'))
            row += 1
