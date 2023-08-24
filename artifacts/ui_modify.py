# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'modify.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(321, 660)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 140, 315, 30))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 208, 315, 31))
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, 490, 315, 31))
        self.objectText = QLineEdit(Form)
        self.objectText.setObjectName(u"objectText")
        self.objectText.setGeometry(QRect(0, 39, 315, 26))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 270, 315, 31))
        self.locationText = QLineEdit(Form)
        self.locationText.setObjectName(u"locationText")
        self.locationText.setGeometry(QRect(0, 176, 315, 26))
        self.label_8 = QLabel(Form)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 340, 315, 31))
        self.actionBox = QComboBox(Form)
        self.actionBox.setObjectName(u"actionBox")
        self.actionBox.setGeometry(QRect(0, 450, 311, 31))
        self.calibrationText = QLineEdit(Form)
        self.calibrationText.setObjectName(u"calibrationText")
        self.calibrationText.setGeometry(QRect(0, 245, 315, 26))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 2, 315, 31))
        self.label_7 = QLabel(Form)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 421, 315, 31))
        self.quantityText = QLineEdit(Form)
        self.quantityText.setObjectName(u"quantityText")
        self.quantityText.setGeometry(QRect(0, 310, 315, 26))
        self.categoryBox = QComboBox(Form)
        self.categoryBox.setObjectName(u"categoryBox")
        self.categoryBox.setGeometry(QRect(0, 380, 311, 31))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 71, 315, 31))
        self.projectBox = QComboBox(Form)
        self.projectBox.setObjectName(u"projectBox")
        self.projectBox.setGeometry(QRect(0, 530, 311, 31))
        self.TypeBox = QComboBox(Form)
        self.TypeBox.setObjectName(u"TypeBox")
        self.TypeBox.setEnabled(True)
        self.TypeBox.setGeometry(QRect(0, 100, 311, 31))
        self.cancelButton = QPushButton(Form)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(0, 620, 315, 29))
        self.insertButton = QPushButton(Form)
        self.insertButton.setObjectName(u"insertButton")
        self.insertButton.setGeometry(QRect(0, 580, 315, 29))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Location", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Calibration", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Project", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Quantity", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Category", None))
        self.label.setText(QCoreApplication.translate("Form", u"Object", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Action", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Type", None))
        self.cancelButton.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.insertButton.setText(QCoreApplication.translate("Form", u"Update", None))
    # retranslateUi

