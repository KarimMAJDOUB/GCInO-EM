from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
#from authenticate import login

class SignOutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Sign Out")
        
        layout = QVBoxLayout()
        self.label = QLabel("Are you sure you want to sign out?")
        layout.addWidget(self.label)
        
        self.sign_out_button = QPushButton("Yes")
        self.sign_out_button.clicked.connect(self.sign_out)
        layout.addWidget(self.sign_out_button)
        
        self.cancel_button = QPushButton("No")
        self.cancel_button.clicked.connect(self.close)
        layout.addWidget(self.cancel_button)
        
        self.setLayout(layout)

    def sign_out(self):
        """
        """
        #QApplication.quit()
        """form1 = login()
        form1.show()
        self.hide()"""