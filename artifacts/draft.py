import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QTextEdit, QLabel, QWidget
from PyQt5.QtCore import Qt

class CharacterCounter(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Character Counter")

        layout = QVBoxLayout()

        self.text_edit = QTextEdit()
        layout.addWidget(self.text_edit)

        self.character_count_label = QLabel("0/1000")
        layout.addWidget(self.character_count_label, alignment=Qt.AlignHCenter)

        self.text_edit.textChanged.connect(self.update_character_count)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def update_character_count(self):
        character_count = len(self.text_edit.toPlainText())
        self.character_count_label.setText(f"{character_count}/1000")

        if character_count > 10:
            self.character_count_label.setStyleSheet("color: red;")
            self.text_edit.setReadOnly(True)  # Désactiver la saisie
        else:
            self.character_count_label.setStyleSheet("color: black;")
            self.text_edit.setReadOnly(False)  # Activer la saisie

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CharacterCounter()
    window.show()
    sys.exit(app.exec_())
