# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plot_activ.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QPushButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1264, 779)
        self.project_box = QComboBox(Form)
        self.project_box.setObjectName(u"project_box")
        self.project_box.setGeometry(QRect(10, 10, 211, 31))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 70, 571, 311))
        self.widget_2 = QWidget(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setEnabled(True)
        self.widget_2.setGeometry(QRect(600, 70, 641, 311))
        self.widget_3 = QWidget(Form)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setEnabled(True)
        self.widget_3.setGeometry(QRect(0, 400, 561, 371))
        self.widget_4 = QWidget(Form)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setEnabled(True)
        self.widget_4.setGeometry(QRect(580, 400, 661, 371))
        self.person_box = QComboBox(Form)
        self.person_box.setObjectName(u"person_box")
        self.person_box.setGeometry(QRect(250, 10, 211, 31))
        self.object_box = QComboBox(Form)
        self.object_box.setObjectName(u"object_box")
        self.object_box.setGeometry(QRect(490, 10, 211, 31))
        self.export_btn = QPushButton(Form)
        self.export_btn.setObjectName(u"export_btn")
        self.export_btn.setGeometry(QRect(720, 10, 151, 31))
        self.export_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.export_btn.setText(QCoreApplication.translate("Form", u"Export Report", None))
    # retranslateUi

