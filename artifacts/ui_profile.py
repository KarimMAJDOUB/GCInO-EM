# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'profile.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGroupBox,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(417, 380)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 10, 381, 361))
        self.groupBox.setLayoutDirection(Qt.LeftToRight)
        self.groupBox.setAutoFillBackground(False)
        self.groupBox.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.groupBox.setFlat(False)
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 110, 81, 20))
        self.lastNameTextField = QLineEdit(self.groupBox)
        self.lastNameTextField.setObjectName(u"lastNameTextField")
        self.lastNameTextField.setGeometry(QRect(150, 70, 211, 20))
        self.emailTextField = QLineEdit(self.groupBox)
        self.emailTextField.setObjectName(u"emailTextField")
        self.emailTextField.setGeometry(QRect(150, 110, 211, 20))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 70, 81, 20))
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 150, 81, 20))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 30, 81, 20))
        self.firstNameTextField = QLineEdit(self.groupBox)
        self.firstNameTextField.setObjectName(u"firstNameTextField")
        self.firstNameTextField.setGeometry(QRect(150, 30, 211, 20))
        self.usernameTextField = QLineEdit(self.groupBox)
        self.usernameTextField.setObjectName(u"usernameTextField")
        self.usernameTextField.setGeometry(QRect(150, 150, 211, 20))
        self.saveButton = QPushButton(self.groupBox)
        self.saveButton.setObjectName(u"saveButton")
        self.saveButton.setGeometry(QRect(280, 320, 75, 23))
        self.usernameTextField_2 = QLineEdit(self.groupBox)
        self.usernameTextField_2.setObjectName(u"usernameTextField_2")
        self.usernameTextField_2.setGeometry(QRect(150, 190, 211, 20))
        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 190, 81, 20))
        self.label_6 = QLabel(self.groupBox)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(30, 230, 81, 20))
        self.usernameTextField_3 = QLineEdit(self.groupBox)
        self.usernameTextField_3.setObjectName(u"usernameTextField_3")
        self.usernameTextField_3.setGeometry(QRect(150, 230, 211, 20))
        self.label_7 = QLabel(self.groupBox)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 270, 111, 20))
        self.comboBox = QComboBox(self.groupBox)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEnabled(True)
        self.comboBox.setGeometry(QRect(150, 270, 211, 22))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Profile Information", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Profile Data", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Email", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Last name", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"First name", None))
        self.usernameTextField.setText("")
        self.saveButton.setText(QCoreApplication.translate("Dialog", u"Save", None))
        self.usernameTextField_2.setText("")
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Society", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Entity", None))
        self.usernameTextField_3.setText("")
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Current Projects", None))
        self.comboBox.setCurrentText("")
    # retranslateUi

