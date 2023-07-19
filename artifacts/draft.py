import mysql.connector
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTreeView, QTableWidget, QTableWidgetItem, QPushButton
from PyQt6.QtGui import QStandardItem, QStandardItemModel


class WidgetExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table = QTableWidget()
        self.tree_view = QTreeView()
        self.reset_button = QPushButton("Reset")

        layout = QVBoxLayout()
        layout.addWidget(self.table)
        layout.addWidget(self.tree_view)
        layout.addWidget(self.reset_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Initialize the QStandardItemModel
        self.model = QStandardItemModel()
        self.tree_view.setModel(self.model)

        # Connect the tree view's item selection signal to the slot
        self.tree_view.selectionModel().selectionChanged.connect(self.handle_item_selection)

        self.reset_button.clicked.connect(self.reset)

        # Populate the tree view
        self.populate_tree()

        # Connect to MySQL database
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Krayem99882056&&&",
            database="fakegcino"
        )

        # Populate the initial table data
        initial_data = [
            ["Data 1", "Data 2", "Data 3"],
            ["Data 4", "Data 5", "Data 6"],
            ["Data 7", "Data 8", "Data 9"]
        ]
        self.populate_table(initial_data)

    def populate_tree(self):
        # Example tree data
        data = {
            'Category 1': ['Item 1', 'Item 2'],
            'Category 2': ['Item 3', 'Item 4'],
            'Category 3': ['Item 5', 'Item 6']
        }

        # Clear any existing data in the model
        self.model.clear()

        # Create the root item
        root = self.model.invisibleRootItem()

        # Populate the tree view
        for category, items in data.items():
            category_item = QStandardItem(category)
            root.appendRow(category_item)
            for item in items:
                item_item = QStandardItem(item)
                category_item.appendRow(item_item)

    def populate_table(self, data):
        self.table.clearContents()
        self.table.setRowCount(len(data))
        self.table.setColumnCount(len(data[0]))

        for row in range(len(data)):
            for col in range(len(data[0])):
                item = QTableWidgetItem(data[row][col])
                self.table.setItem(row, col, item)

    def handle_item_selection(self, selected, deselected):
        selected_indexes = selected.indexes()
        if selected_indexes:
            selected_item = selected_indexes[0].data()
            # Update the table based on the selected item
            if selected_item == 'Item 1':
                query = "SELECT Object, Type_Object, Location FROM object_dist WHERE Type_Object='Consumable'"
            elif selected_item == 'Item 2':
                query = "SELECT Object, Type_Object, Location FROM object_dist WHERE Type_object='Tooling'"
            elif selected_item == 'Item 3':
                query = "SELECT Object, Type_Object, Location FROM object_dist WHERE Object='iPhone'"
            else:
                query = ""

            if query:
                cursor = self.db.cursor()
                cursor.execute(query)
                result = cursor.fetchall()
                self.populate_table(result)

    def reset(self):
        # Clear any selection in the tree view
        self.tree_view.clearSelection()

        # Reset the table with initial data
        initial_data = [
            ["Data 1", "Data 2", "Data 3"],
            ["Data 4", "Data 5", "Data 6"],
            ["Data 7", "Data 8", "Data 9"]
        ]
        self.populate_table(initial_data)


if __name__ == "__main__":
    app = QApplication([])
    window = WidgetExample()
    window.show()
    app.exec()
