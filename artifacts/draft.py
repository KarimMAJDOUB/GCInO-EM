import openpyxl


import subprocess


import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt

# Fonction pour ouvrir un fichier Excel
def open_excel_file(row, col):
    excel_exe = r'C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE'
    if col == 0:  # Colonne des noms de fichiers
        file_name = table_widget.item(row, col).text()
        file_path = os.path.join(directory_path, file_name)
        
        if os.path.exists(file_path):
            subprocess.run(f'start "" "{excel_exe}" "{file_path}"', shell=True)
        else:
            print(f"Le fichier {file_path} n'existe pas.")

# Créer une application Qt
app = QApplication([])

# Créer la fenêtre principale
window = QMainWindow()
table_widget = QTableWidget()
window.setCentralWidget(table_widget)

# Chemin vers le répertoire contenant les fichiers Excel
directory_path = './Bordoreau/'

# Lister les fichiers Excel dans le répertoire
excel_files = [f for f in os.listdir(directory_path) if f.endswith(".xlsx")]

# Remplir la première colonne du QTableWidget avec les noms des fichiers Excel
table_widget.setColumnCount(1)  # Une seule colonne
table_widget.setRowCount(len(excel_files))  # Nombre de lignes

for row, excel_file in enumerate(excel_files):
    item = QTableWidgetItem(excel_file)
    table_widget.setItem(row, 0, item)

# Connecter le signal cellClicked à la fonction pour ouvrir le fichier
table_widget.cellClicked.connect(open_excel_file)

# Afficher la fenêtre
window.show()

# Lancer l'application Qt
app.exec_()


