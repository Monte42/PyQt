from PyQt6.QtWidgets import QDockWidget, QTableWidgetItem
from PyQt6 import uic
from MySQLdb import _mysql

class RightDock(QDockWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./gui/rightDock.ui', self)
        self.updateBtn.clicked.connect(self.updateData)

        self.getHellos()

    def getHellos(self):
        # Connect to db
        db = _mysql.connect('localhost','root','root','pyqt6')
        # run query
        db.query("""SELECT * FROM hellos;""")
        # store results into var - This returns a model object
        results = db.store_result()
        # fetch data from object - takes 2 arguments(maxrows,how)
        # Max rows sets a limit to the rows, may return less, 0 returns all
        # how is the format data is returned
            # 0 is a tuple
            # 1 is a dict where keys are the col or tabel.com (joins)
            # 2 is a dict where keys are strictly the col
        all_hellos = results.fetch_row(0,1)
        # setting Table row count to results list length
        self.tableHello.setRowCount(len(all_hellos))
        row = 0
        for hello in all_hellos:
            # setItem(number_of_row, number_of_col, item) item must be QTableWidget
            # results comes as bytes, .decode("utf-8") converts it to a string
            self.tableHello.setItem(row, 0, QTableWidgetItem(hello["name"].decode("utf-8")))
            self.tableHello.setItem(row, 1, QTableWidgetItem(hello["message"].decode("utf-8")))
            self.tableHello.setItem(row, 2, QTableWidgetItem(hello["created_at"].decode("utf-8")))
            row += 1

    def updateData(self):
        self.getHellos()