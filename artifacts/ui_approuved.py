# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'approuved.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(409, 609)
        self.cout = QLineEdit(Form)
        self.cout.setObjectName(u"cout")
        self.cout.setGeometry(QRect(100, 30, 281, 31))
        self.label_11 = QLabel(Form)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 29, 61, 31))
        self.label_12 = QLabel(Form)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(10, 190, 61, 31))
        self.quantity = QLineEdit(Form)
        self.quantity.setObjectName(u"quantity")
        self.quantity.setGeometry(QRect(100, 110, 281, 31))
        self.gener_br_btn = QPushButton(Form)
        self.gener_br_btn.setObjectName(u"gener_br_btn")
        self.gener_br_btn.setGeometry(QRect(190, 550, 211, 41))
        self.gener_br_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_13 = QLabel(Form)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 110, 61, 31))
        self.link = QLineEdit(Form)
        self.link.setObjectName(u"link")
        self.link.setGeometry(QRect(100, 190, 281, 31))
        self.label_14 = QLabel(Form)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 250, 111, 31))
        self.description = QPlainTextEdit(Form)
        self.description.setObjectName(u"description")
        self.description.setGeometry(QRect(10, 290, 371, 251))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.cout.setText("")
        self.label_11.setText(QCoreApplication.translate("Form", u"Price :", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"Source", None))
        self.quantity.setText("")
        self.gener_br_btn.setText(QCoreApplication.translate("Form", u"Generate Bordoreau", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Quantity", None))
        self.link.setText("")
        self.label_14.setText(QCoreApplication.translate("Form", u"Description : ", None))
    # retranslateUi

