import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Connexion à la base de données MySQL
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Krayem99882056&&&",
            database="fakegcino"
        )

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 800, 600)
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(50, 50, 700, 500)
        
        # Charger les données initiales
        self.loadTableData()

    def loadTableData(self):
        cursor = self.conn.cursor()
        query = "SELECT * FROM orders"
        cursor.execute(query)
        result = cursor.fetchall()

        # Effacer les données actuellement affichées
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        
        # Ajouter les en-têtes de colonnes
        column_headers = [desc[0] for desc in cursor.description]
        self.tableWidget.setColumnCount(len(column_headers))
        self.tableWidget.setHorizontalHeaderLabels(column_headers)

        # Ajouter les données au QTableWidget
        for row_number, row_data in enumerate(result):
            self.tableWidget.insertRow(row_number)
            for col_number, cell_data in enumerate(row_data):
                self.tableWidget.setItem(row_number, col_number, QTableWidgetItem(str(cell_data)))

        cursor.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
