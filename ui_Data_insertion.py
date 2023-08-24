# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Data_insertion.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(344, 671)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 2, 315, 31))
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 71, 315, 31))
        self.calibrationText = QLineEdit(Dialog)
        self.calibrationText.setObjectName(u"calibrationText")
        self.calibrationText.setGeometry(QRect(10, 245, 315, 26))
        self.locationText = QLineEdit(Dialog)
        self.locationText.setObjectName(u"locationText")
        self.locationText.setGeometry(QRect(10, 176, 315, 26))
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 208, 315, 31))
        self.objectText = QLineEdit(Dialog)
        self.objectText.setObjectName(u"objectText")
        self.objectText.setGeometry(QRect(10, 39, 315, 26))
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 140, 315, 30))
        self.TypeBox = QComboBox(Dialog)
        self.TypeBox.addItem("")
        self.TypeBox.addItem("")
        self.TypeBox.setObjectName(u"TypeBox")
        self.TypeBox.setGeometry(QRect(10, 100, 311, 31))
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 270, 315, 31))
        self.quantityText = QLineEdit(Dialog)
        self.quantityText.setObjectName(u"quantityText")
        self.quantityText.setGeometry(QRect(10, 310, 315, 26))
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 490, 315, 31))
        self.projectBox = QComboBox(Dialog)
        self.projectBox.setObjectName(u"projectBox")
        self.projectBox.setGeometry(QRect(10, 530, 311, 31))
        self.cancelButton = QPushButton(Dialog)
        self.cancelButton.setObjectName(u"cancelButton")
        self.cancelButton.setGeometry(QRect(10, 620, 315, 29))
        self.cancelButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.insertButton = QPushButton(Dialog)
        self.insertButton.setObjectName(u"insertButton")
        self.insertButton.setGeometry(QRect(10, 580, 315, 29))
        self.insertButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 421, 315, 31))
        self.actionBox = QComboBox(Dialog)
        self.actionBox.setObjectName(u"actionBox")
        self.actionBox.setGeometry(QRect(10, 450, 311, 31))
        self.categoryBox = QComboBox(Dialog)
        self.categoryBox.setObjectName(u"categoryBox")
        self.categoryBox.setGeometry(QRect(10, 380, 311, 31))
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(10, 340, 315, 31))
        self.updateButton = QPushButton(Dialog)
        self.updateButton.setObjectName(u"updateButton")
        self.updateButton.setEnabled(True)
        self.updateButton.setGeometry(QRect(10, 580, 315, 29))
        self.updateButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Object", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Type", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Calibration", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Location", None))
        self.TypeBox.setItemText(0, QCoreApplication.translate("Dialog", u"Consumable", None))
        self.TypeBox.setItemText(1, QCoreApplication.translate("Dialog", u"Tooling", None))

        self.label_6.setText(QCoreApplication.translate("Dialog", u"Quantity", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Project", None))
        self.cancelButton.setText(QCoreApplication.translate("Dialog", u"Cancel", None))
        self.insertButton.setText(QCoreApplication.translate("Dialog", u"Insert", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Action", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Category", None))
        self.updateButton.setText(QCoreApplication.translate("Dialog", u"Update", None))
    # retranslateUi

