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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCalendarWidget, QComboBox,
    QFrame, QGridLayout, QGroupBox, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QToolBox, QTreeWidget, QTreeWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1188, 644)
        Form.setLayoutDirection(Qt.LeftToRight)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.widget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setEnabled(True)
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
        self.treeWidget.setGeometry(QRect(11, 43, 256, 192))
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
        self.tableWidget.setGeometry(QRect(385, 11, 256, 192))
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
        self.insertDataButton.setGeometry(QRect(760, 489, 93, 29))
        self.insertDataButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_7 = QPushButton(self.Tab1)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(760, 448, 93, 29))
        self.reset_btn = QPushButton(self.Tab1)
        self.reset_btn.setObjectName(u"reset_btn")
        self.reset_btn.setGeometry(QRect(11, 527, 93, 29))
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
        self.treeWidget_2.setGeometry(QRect(11, 445, 367, 75))
        self.treeWidget_2.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))
        self.search = QLineEdit(self.Tab1)
        self.search.setObjectName(u"search")
        self.search.setGeometry(QRect(11, 11, 149, 25))
        self.toolBox = QToolBox(self.Tab1)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setGeometry(QRect(760, 43, 73, 143))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 73, 73))
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
        self.page_2.setGeometry(QRect(0, 0, 73, 73))
        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 120, 351))
        self.frame.setContextMenuPolicy(Qt.NoContextMenu)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        icon2 = QIcon()
        icon2.addFile(u"../../../../../Downloads/chevron-up.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.toolBox.addItem(self.page_2, icon2, u"")
        self.tabWidget.addTab(self.Tab1, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_4 = QGridLayout(self.tab_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.Why_Box = QComboBox(self.tab_3)
        self.Why_Box.setObjectName(u"Why_Box")

        self.gridLayout_4.addWidget(self.Why_Box, 0, 1, 1, 1)

        self.What_Box = QComboBox(self.tab_3)
        self.What_Box.setObjectName(u"What_Box")

        self.gridLayout_4.addWidget(self.What_Box, 0, 2, 1, 1)

        self.Who_Box = QComboBox(self.tab_3)
        self.Who_Box.setObjectName(u"Who_Box")

        self.gridLayout_4.addWidget(self.Who_Box, 0, 3, 1, 1)

        self.date_Box = QComboBox(self.tab_3)
        self.date_Box.setObjectName(u"date_Box")

        self.gridLayout_4.addWidget(self.date_Box, 0, 4, 1, 1)

        self.action_box = QComboBox(self.tab_3)
        self.action_box.setObjectName(u"action_box")

        self.gridLayout_4.addWidget(self.action_box, 0, 5, 1, 1)

        self.calendar_label = QLabel(self.tab_3)
        self.calendar_label.setObjectName(u"calendar_label")
        font = QFont()
        font.setUnderline(True)
        self.calendar_label.setFont(font)
        self.calendar_label.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.calendar_label, 0, 6, 1, 1)

        self.calendar = QCalendarWidget(self.tab_3)
        self.calendar.setObjectName(u"calendar")

        self.gridLayout_4.addWidget(self.calendar, 1, 5, 1, 2)

        self.btn_plot_act = QPushButton(self.tab_3)
        self.btn_plot_act.setObjectName(u"btn_plot_act")
        self.btn_plot_act.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.btn_plot_act, 2, 0, 1, 1)

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
        self.tableWidget_2.setSizeIncrement(QSize(0, 0))
        self.tableWidget_2.setStyleSheet(u"QTableWidget{\n"
"setColumnCount(4)\n"
"setColumnWidth(0, 200)\n"
"setColumnWidth(1, 200)\n"
"setColumnWidth(2, 200)\n"
"setColumnWidth(3, 200)\n"
"}")

        self.gridLayout_4.addWidget(self.tableWidget_2, 2, 1, 2, 6)

        self.export_csv_btn = QPushButton(self.tab_3)
        self.export_csv_btn.setObjectName(u"export_csv_btn")
        self.export_csv_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_4.addWidget(self.export_csv_btn, 3, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_6 = QGridLayout(self.tab_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.groupBox = QGroupBox(self.tab_2)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_5 = QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.request = QLineEdit(self.groupBox)
        self.request.setObjectName(u"request")

        self.gridLayout_5.addWidget(self.request, 0, 1, 1, 3)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 1, 0, 1, 1)

        self.name = QLineEdit(self.groupBox)
        self.name.setObjectName(u"name")

        self.gridLayout_5.addWidget(self.name, 1, 1, 1, 3)

        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_5.addWidget(self.label_4, 2, 0, 1, 1)

        self.quantity = QLineEdit(self.groupBox)
        self.quantity.setObjectName(u"quantity")

        self.gridLayout_5.addWidget(self.quantity, 2, 1, 1, 3)

        self.label_5 = QLabel(self.groupBox)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_5.addWidget(self.label_5, 3, 0, 1, 1)

        self.cout = QLineEdit(self.groupBox)
        self.cout.setObjectName(u"cout")

        self.gridLayout_5.addWidget(self.cout, 3, 1, 1, 3)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_5.addWidget(self.label_3, 4, 0, 1, 2)

        self.description = QTextEdit(self.groupBox)
        self.description.setObjectName(u"description")

        self.gridLayout_5.addWidget(self.description, 5, 0, 1, 4)

        self.count_label = QLabel(self.groupBox)
        self.count_label.setObjectName(u"count_label")

        self.gridLayout_5.addWidget(self.count_label, 6, 0, 1, 2)

        self.send_btn = QPushButton(self.groupBox)
        self.send_btn.setObjectName(u"send_btn")
        self.send_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.send_btn, 6, 2, 1, 1)

        self.clear_btn = QPushButton(self.groupBox)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setCursor(QCursor(Qt.PointingHandCursor))

        self.gridLayout_5.addWidget(self.clear_btn, 6, 3, 1, 1)


        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 1)

        self.table_user = QTableWidget(self.tab_2)
        if (self.table_user.columnCount() < 2):
            self.table_user.setColumnCount(2)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_user.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_user.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        self.table_user.setObjectName(u"table_user")

        self.gridLayout_6.addWidget(self.table_user, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.gridLayout_8 = QGridLayout(self.tab_5)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.groupBox_2 = QGroupBox(self.tab_5)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_7 = QGridLayout(self.groupBox_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.table_warehouseman = QTableWidget(self.groupBox_2)
        if (self.table_warehouseman.columnCount() < 7):
            self.table_warehouseman.setColumnCount(7)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_warehouseman.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_warehouseman.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_warehouseman.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_warehouseman.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_warehouseman.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_warehouseman.setHorizontalHeaderItem(5, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_warehouseman.setHorizontalHeaderItem(6, __qtablewidgetitem23)
        self.table_warehouseman.setObjectName(u"table_warehouseman")

        self.gridLayout_7.addWidget(self.table_warehouseman, 0, 0, 1, 1)


        self.gridLayout_8.addWidget(self.groupBox_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.gridLayout_9 = QGridLayout(self.tab_6)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.table_manager = QTableWidget(self.tab_6)
        if (self.table_manager.columnCount() < 2):
            self.table_manager.setColumnCount(2)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_manager.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_manager.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        self.table_manager.setObjectName(u"table_manager")
        self.table_manager.viewport().setProperty("cursor", QCursor(Qt.PointingHandCursor))

        self.gridLayout_9.addWidget(self.table_manager, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_6, "")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)


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
        self.profileButton.setText(QCoreApplication.translate("Form", u"Profil", None))
        self.projectButton.setText(QCoreApplication.translate("Form", u"Projects", None))
        self.signoutButton.setText(QCoreApplication.translate("Form", u"Sign Out", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("Form", u"User", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), "")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Tab1), QCoreApplication.translate("Form", u"Visualization", None))
        self.Why_Box.setCurrentText("")
        self.What_Box.setCurrentText("")
        self.calendar_label.setText(QCoreApplication.translate("Form", u"Calendar", None))
        self.btn_plot_act.setText(QCoreApplication.translate("Form", u"Tendency", None))
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
        self.export_csv_btn.setText(QCoreApplication.translate("Form", u"Export_csv", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("Form", u"History and Tendency", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("Form", u"Tools localisation", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"User", None))
        self.label.setText(QCoreApplication.translate("Form", u"Request : ", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Name : ", None))
        self.name.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Quantity : ", None))
        self.quantity.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Price :", None))
        self.cout.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"Description : ", None))
        self.count_label.setText(QCoreApplication.translate("Form", u"0/1000", None))
        self.send_btn.setText(QCoreApplication.translate("Form", u"Send", None))
        self.clear_btn.setText(QCoreApplication.translate("Form", u"Clear", None))
        ___qtablewidgetitem15 = self.table_user.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Form", u"Request", None));
        ___qtablewidgetitem16 = self.table_user.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Form", u"State", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"Orders", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"warehouseman", None))
        ___qtablewidgetitem17 = self.table_warehouseman.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Form", u"id", None));
        ___qtablewidgetitem18 = self.table_warehouseman.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("Form", u"Order", None));
        ___qtablewidgetitem19 = self.table_warehouseman.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("Form", u"Object", None));
        ___qtablewidgetitem20 = self.table_warehouseman.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("Form", u"Sender", None));
        ___qtablewidgetitem21 = self.table_warehouseman.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("Form", u"Status", None));
        ___qtablewidgetitem22 = self.table_warehouseman.horizontalHeaderItem(5)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("Form", u"Actions", None));
        ___qtablewidgetitem23 = self.table_warehouseman.horizontalHeaderItem(6)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("Form", u"Add to Panel", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("Form", u"Orders-Warehouseman", None))
        ___qtablewidgetitem24 = self.table_manager.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("Form", u"Bordoreau", None));
        ___qtablewidgetitem25 = self.table_manager.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("Form", u"Action", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("Form", u"Orders-Manager", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Help", None))
    # retranslateUi

