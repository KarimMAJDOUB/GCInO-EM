from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QCalendarWidget
from PyQt5.QtCore import QDate, Qt
from PyQt5.QtGui import QColor, QPainter

class DateRangePicker(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Date Range Picker")
        layout = QVBoxLayout()

        self.calendar = CustomCalendarWidget(self)
        #self.calendar.setSelectionMode(QCalendarWidget.SingleSelection)  # Désactiver la sélection de multiples dates
        self.calendar.selectionChanged.connect(self.handle_selection_changed)
        layout.addWidget(self.calendar)

        self.label = QLabel(self)
        layout.addWidget(self.label)

        self.start_date = None
        self.end_date = None

        self.setLayout(layout)

    def handle_selection_changed(self):
        selected_date = self.calendar.selectedDate()
        if not self.start_date:
            self.start_date = selected_date
            self.end_date = None
        elif not self.end_date:
            self.end_date = selected_date
            self.highlight_dates_between_selections()
        else:
            self.start_date = selected_date
            self.end_date = None
            self.highlight_dates_between_selections()

    def highlight_dates_between_selections(self):
        if not self.start_date or not self.end_date:
            return

        current_date = self.calendar.minimumDate()
        last_date = self.calendar.maximumDate()
        while current_date <= last_date:
            if self.start_date <= current_date <= self.end_date:
                self.calendar.set_date_background(current_date, QColor(100, 149, 237))  # Couleur de sélection
            else:
                self.calendar.set_date_background(current_date, None)
            current_date = current_date.addDays(1)

        self.calendar.updateCells()

    def filterBox(self):
        # Votre logique de filtre ici
        pass

class CustomCalendarWidget(QCalendarWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Définir les dates minimale et maximale ici (facultatif)
        self.setMinimumDate(QDate(2021, 1, 1))
        self.setMaximumDate(QDate(2023, 12, 31))

        # Dictionnaire pour stocker les dates avec leurs arrière-plans personnalisés
        self.date_backgrounds = {}

    def set_date_background(self, date, background):
        self.date_backgrounds[date] = background

    def paintCell(self, painter, rect, date):
        # Sauvegarder l'état du painter
        painter.save()

        # Dessiner le fond de la cellule
        background = self.date_backgrounds.get(date)
        if background:
            painter.fillRect(rect, background)

        # Appel à la méthode paintCell de la classe de base pour dessiner le texte
        super().paintCell(painter, rect, date)

        # Restaurer l'état du painter
        painter.restore()

if __name__ == "__main__":
    app = QApplication([])
    window = DateRangePicker()
    window.show()
    app.exec_()
