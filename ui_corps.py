# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'corps.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QHeaderView, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QToolBox, QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1518, 661)
        Form.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
        self.tabWidget.setGeometry(QRect(30, 10, 1551, 661))
        self.Tab1 = QWidget()
        self.Tab1.setObjectName(u"Tab1")
        self.treeWidget = QTreeWidget(self.Tab1)
        icon = QIcon()
        iconThemeName = u"printer"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u".", QSize(), QIcon.Normal, QIcon.Off)

        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem1 = QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        __qtreewidgetitem2 = QTreeWidgetItem(__qtreewidgetitem)
        __qtreewidgetitem2.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEditable|Qt.ItemIsDragEnabled|Qt.ItemIsDropEnabled|Qt.ItemIsUserCheckable|Qt.ItemIsEnabled);
        __qtreewidgetitem2.setIcon(0, icon);
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(__qtreewidgetitem2)
        QTreeWidgetItem(self.treeWidget)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(0, 50, 171, 351))
        self.treeWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.treeWidget.setLayoutDirection(Qt.LeftToRight)
        self.treeWidget.setAutoFillBackground(False)
        self.treeWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget = QTableWidget(self.Tab1)
        if (self.tableWidget.columnCount() < 6):
            self.tableWidget.setColumnCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(200, 20, 750, 551))
        self.tableWidget.setSizeIncrement(QSize(0, 0))
        self.tableWidget.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"setColumnCount(4)\n"
"setColumnWidth(0, 200)\n"
"setColumnWidth(1, 200)\n"
"setColumnWidth(2, 200)\n"
"setColumnWidth(3, 200)\n"
"}")
        self.insertDataButton = QPushButton(self.Tab1)
        self.insertDataButton.setObjectName(u"insertDataButton")
        self.insertDataButton.setGeometry(QRect(960, 530, 161, 41))
        self.insertDataButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7 = QPushButton(self.Tab1)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(960, 470, 161, 41))
        self.toolBox = QToolBox(self.Tab1)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setGeometry(QRect(1120, 10, 127, 251))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 127, 181))
        self.profileButton = QPushButton(self.page)
        self.profileButton.setObjectName(u"profileButton")
        self.profileButton.setGeometry(QRect(0, 30, 141, 31))
        self.profileButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.projectButton = QPushButton(self.page)
        self.projectButton.setObjectName(u"projectButton")
        self.projectButton.setGeometry(QRect(0, 90, 131, 31))
        self.projectButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.signoutButton = QPushButton(self.page)
        self.signoutButton.setObjectName(u"signoutButton")
        self.signoutButton.setGeometry(QRect(0, 150, 131, 31))
        icon1 = QIcon()
        icon1.addFile(u"../../../../../Downloads/abstract-user-flat-1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page, icon1, u"User")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 127, 181))
        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 120, 351))
        self.frame.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        icon2 = QIcon()
        icon2.addFile(u"../../../../../Downloads/chevron-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_2, icon2, u"")
        self.reset_btn = QPushButton(self.Tab1)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setGeometry(QRect(0, 550, 171, 21))
        self.reset_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.treeWidget_2 = QTreeWidget(self.Tab1)
        __qtreewidgetitem3 = QTreeWidgetItem(self.treeWidget_2)
        __qtreewidgetitem4 = QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem4)
        QTreeWidgetItem(__qtreewidgetitem4)
        __qtreewidgetitem5 = QTreeWidgetItem(__qtreewidgetitem3)
        QTreeWidgetItem(__qtreewidgetitem5)
        QTreeWidgetItem(__qtreewidgetitem5)
        QTreeWidgetItem(self.treeWidget_2)
        self.treeWidget_2.setObjectName(u"treeWidget_2")
        self.treeWidget_2.setGeometry(QRect(0, 400, 171, 141))
        self.treeWidget_2.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.search = QLineEdit(self.Tab1)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(0, 20, 171, 21))
        self.tabWidget.addTab(self.Tab1, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tableWidget_2 = QTableWidget(self.tab_3)
        if (self.tableWidget_2.columnCount() < 9):
            self.tableWidget_2.setColumnCount(9)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem14)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(140, 60, 1350, 561))
        self.tableWidget_2.setSizeIncrement(QSize(0, 0))
        self.tableWidget_2.setStyleSheet(u"QTableWidget{\n"
"setColumnCount(4)\n"
"setColumnWidth(0, 200)\n"
"setColumnWidth(1, 200)\n"
"setColumnWidth(2, 200)\n"
"setColumnWidth(3, 200)\n"
"}")
        self.btn_plot_act = QPushButton(self.tab_3)
        self.btn_plot_act.setObjectName(u"btn_plot_act")
        self.btn_plot_act.setGeometry(QRect(10, 60, 121, 81))
        self.btn_plot_act.setCursor(QCursor(Qt.PointingHandCursor))
        self.Why_Box = QComboBox(self.tab_3)
        self.Why_Box.setObjectName(u"Why_Box")
        self.Why_Box.setGeometry(QRect(560, 0, 121, 31))
        self.Who_Box = QComboBox(self.tab_3)
        self.Who_Box.setObjectName(u"Who_Box")
        self.Who_Box.setGeometry(QRect(850, 0, 171, 31))
        self.What_Box = QComboBox(self.tab_3)
        self.What_Box.setObjectName(u"What_Box")
        self.What_Box.setGeometry(QRect(700, 0, 121, 31))
        self.date_Box = QComboBox(self.tab_3)
        self.date_Box.setObjectName(u"date_Box")
        self.date_Box.setGeometry(QRect(1030, 0, 151, 31))
        self.action_box = QComboBox(self.tab_3)
        self.action_box.setObjectName(u"action_box")
        self.action_box.setGeometry(QRect(1190, 0, 101, 31))
        self.export_csv_btn = QPushButton(self.tab_3)
        self.export_csv_btn.setObjectName(u"export_csv_btn")
        self.export_csv_btn.setGeometry(QRect(10, 160, 121, 81))
        self.export_csv_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        self.tabWidget.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.tabWidget.setWhatsThis(QCoreApplication.translate("Form", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"Objects", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Form", u"Category 01", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Form", u"Type 01", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("Form", u"Object 01", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem2.child(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("Form", u"Object 02", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem1.child(1)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("Form", u"Type 02", None));
        ___qtreewidgetitem6 = ___qtreewidgetitem5.child(0)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("Form", u"Object 03", None));
        ___qtreewidgetitem7 = ___qtreewidgetitem5.child(1)
        ___qtreewidgetitem7.setText(0, QCoreApplication.translate("Form", u"Object 04", None));
        ___qtreewidgetitem8 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem8.setText(0, QCoreApplication.translate("Form", u"Category 02", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Object", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Type", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Location", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Calibration", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Quantity", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Category", None));
        self.insertDataButton.setText(QCoreApplication.translate("Form", u"Insert data", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"Verify", None))
        self.profileButton.setText(QCoreApplication.translate("Form", u"Profil", None))
        self.projectButton.setText(QCoreApplication.translate("Form", u"Projects", None))
        self.signoutButton.setText(QCoreApplication.translate("Form", u"Sign Out", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Form", u"User", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), "")
        self.reset_btn.setText(QCoreApplication.translate("Form", u"Reset", None))
        ___qtreewidgetitem9 = self.treeWidget_2.headerItem()
        ___qtreewidgetitem9.setText(0, QCoreApplication.translate("Form", u"Locations", None));

        __sortingEnabled1 = self.treeWidget_2.isSortingEnabled()
        self.treeWidget_2.setSortingEnabled(False)
        ___qtreewidgetitem10 = self.treeWidget_2.topLevelItem(0)
        ___qtreewidgetitem10.setText(0, QCoreApplication.translate("Form", u"Category 01", None));
        ___qtreewidgetitem11 = ___qtreewidgetitem10.child(0)
        ___qtreewidgetitem11.setText(0, QCoreApplication.translate("Form", u"Type 01", None));
        ___qtreewidgetitem12 = ___qtreewidgetitem11.child(0)
        ___qtreewidgetitem12.setText(0, QCoreApplication.translate("Form", u"Object 01", None));
        ___qtreewidgetitem13 = ___qtreewidgetitem11.child(1)
        ___qtreewidgetitem13.setText(0, QCoreApplication.translate("Form", u"Object 02", None));
        ___qtreewidgetitem14 = ___qtreewidgetitem10.child(1)
        ___qtreewidgetitem14.setText(0, QCoreApplication.translate("Form", u"Type 02", None));
        ___qtreewidgetitem15 = ___qtreewidgetitem14.child(0)
        ___qtreewidgetitem15.setText(0, QCoreApplication.translate("Form", u"Object 03", None));
        ___qtreewidgetitem16 = ___qtreewidgetitem14.child(1)
        ___qtreewidgetitem16.setText(0, QCoreApplication.translate("Form", u"Object 04", None));
        ___qtreewidgetitem17 = self.treeWidget_2.topLevelItem(1)
        ___qtreewidgetitem17.setText(0, QCoreApplication.translate("Form", u"Category 02", None));
        self.treeWidget_2.setSortingEnabled(__sortingEnabled1)

        self.search.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab1), QCoreApplication.translate("Form", u"Visualization", None))
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Object", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Type", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Location", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Calibration", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"Action", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"Quantity", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"Name", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"Operation_date", None));
        ___qtablewidgetitem14 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Form", u"Project", None));
        self.btn_plot_act.setText(QCoreApplication.translate("Form", u"Tendency", None))
        self.Why_Box.setCurrentText("")
        self.What_Box.setCurrentText("")
        self.export_csv_btn.setText(QCoreApplication.translate("Form", u"Export_csv", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"History and Tendency", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"Tools localisation", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Orders", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Help", None))
    # retranslateUi

