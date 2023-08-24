# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(328, 440)
        icon = QIcon()
        iconThemeName = u"dialog-password"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        Widget.setWindowIcon(icon)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(Widget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QPushButton#pushButton{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
"	color:rgba(255, 255, 255, 210);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton#pushButton:hover{	\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
"}\n"
"QPushButton#pushButton:pressed{	\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"	background-color:rgba(105, 118, 132, 200);\n"
"}\n"
"\n"
"QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{	\n"
"	background-color: rgba(0, 0, 0, 0);\n"
"	color:rgba(85, 98, 112, 255);\n"
"}\n"
"QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{	\n"
"	color:rgba(155, 168, 182, 220);\n"
"}\n"
"QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{	\n"
"	padding-left:5px;\n"
"	padding-top:5px;"
                        "\n"
"	color:rgba(115, 128, 142, 255);\n"
"}")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(157, 213, 16, 20))
        self.label_4.setStyleSheet(u"border-image: url(:/images/background.png);\n"
"border-radius:20px;")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_8 = QLabel(self.widget)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"color:rgba(255, 255, 255, 210);")

        self.gridLayout_2.addWidget(self.label_8, 0, 1, 1, 1)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        font1 = QFont()
        font1.setPointSize(10)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")

        self.gridLayout_2.addWidget(self.lineEdit, 1, 0, 1, 2)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setStyleSheet(u"background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105, 118, 132, 255);\n"
"color:rgba(255, 255, 255, 230);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.gridLayout_2.addWidget(self.lineEdit_2, 2, 0, 1, 2)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.pushButton.setFont(font2)

        self.gridLayout_2.addWidget(self.pushButton, 3, 0, 1, 2)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 1)

        self.button_2 = QPushButton(self.widget)
        self.button_2.setObjectName(u"button_2")
        font3 = QFont()
        font3.setItalic(True)
        font3.setUnderline(True)
        self.button_2.setFont(font3)
        self.button_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_2.setTabletTracking(False)
        self.button_2.setAutoDefault(False)
        self.button_2.setFlat(True)

        self.gridLayout_2.addWidget(self.button_2, 5, 1, 1, 1)

        self.button = QPushButton(self.widget)
        self.button.setObjectName(u"button")
        self.button.setEnabled(True)
        self.button.setFont(font3)
        self.button.setCursor(QCursor(Qt.PointingHandCursor))
        self.button.setAutoDefault(False)
        self.button.setFlat(True)

        self.gridLayout_2.addWidget(self.button, 6, 1, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


        self.retranslateUi(Widget)

        self.button_2.setDefault(False)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.label_4.setText("")
        self.label_8.setText(QCoreApplication.translate("Widget", u"Log In", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Widget", u"  User Name", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Widget", u"  Password", None))
        self.pushButton.setText(QCoreApplication.translate("Widget", u"L o g  I n", None))
        self.label_6.setText("")
        self.button_2.setText(QCoreApplication.translate("Widget", u"Forget password ?", None))
        self.button.setText(QCoreApplication.translate("Widget", u"You don't have an account yet ?", None))
    # retranslateUi

