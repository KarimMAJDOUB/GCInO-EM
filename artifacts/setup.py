# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
import random
import shutil
import configparser
import subprocess
from PyQt6.QtWidgets import QDialog, QTreeWidgetItem, QMainWindow, QWidget, QTableWidgetItem, QMessageBox, QDialog, QHBoxLayout, QPushButton
from PyQt6.QtGui import QIcon, QColor
from PyQt6.QtCore import Qt
from PyQt6.uic import loadUi
from database import Database
from configparser import ConfigParser
import pymysql.connections as MySQLdb
import csv 
from openpyxl import load_workbook
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class gcinodesign(QDialog):
    def __init__(self, table, table2, tab, calendar_label, calendar, tabwidget):
        """
        """
        super(gcinodesign, self).__init__()
        self.table = table
        self.table2 = table2
        self.tab = tab
        self.calendar_label = calendar_label
        self.calendar = calendar
        self.calendar.setVisible(False)
        self.tabwidget = tabwidget

        #Backend
        self.db = Database()
        config_object = ConfigParser()
        self.path_to_config = "config.ini"
        config_object.read("config.ini")
        userInfo = config_object["USERINFO"]
        self.LOGGED_USER_ID = userInfo["LOGGED_USER_ID"]
        self.LOGGED_USER_ROLE = userInfo["LOGGED_USER_ROLE"]

        self.designTables()
        self.disableTab(self.tab)
        self.designCalendar()
        self.organiseTabsWithRole()

    def designTables(self):
        cols=["Object","Type","Location","Calibration","Quantity", "Category"]
        cols_hist= ["Object","Type","Location","Calibration", "Action", "Quantity", "Name", "Date", "Project"]
        for i in range(len(cols) -1):
            self.table.setColumnWidth(i,150)
        self.table.setColumnWidth(5,1)
        self.table.setHorizontalHeaderLabels(cols)

        for i in range(len(cols_hist)):
            self.table2.setColumnWidth(i,150)
        self.table2.setHorizontalHeaderLabels(cols_hist)

    
    def disableTab(self, widget):
        """
        """
        if self.LOGGED_USER_ROLE == "user":
            for child_widget in widget.findChildren(QWidget):
                child_widget.setVisible(False)
        else:
            for child_widget in widget.findChildren(QWidget):
                child_widget.setVisible(True)
    def organiseTabsWithRole(self):
        """
        """
        if self.LOGGED_USER_ROLE == "user":
            self.tabwidget.removeTab(1)   #History
            self.tabwidget.removeTab(3)   #Order warehouseman
            self.tabwidget.removeTab(3)   #Order manager
        elif self.LOGGED_USER_ROLE == "warehouseman":
            self.tabwidget.removeTab(3)
            self.tabwidget.removeTab(4)
        elif self.LOGGED_USER_ROLE == "manager":
            self.tabwidget.removeTab(3)
            self.tabwidget.removeTab(3)
        else:
            QMessageBox(self, "Error :", "No Role for this user, please check your database")
    
    def designCalendar(self):
        """
        """
        self.calendar_label.mousePressEvent = self.toggleCalendar
    
    def toggleCalendar(self, event):
        """
        """
        self.calendar.setVisible(not self.calendar.isVisible())
        event.accept() 

class gcinotables(QMainWindow):
    def __init__(self, tableWidget, tableWidget2,tableWidget3, tabUser,  btn, type):
        """
        """
        super(gcinotables, self).__init__()
        self.tableWidget = tableWidget
        self.tableWidget_2 = tableWidget2
        self.tableWidget_3 = tableWidget3
        self.tab_user = tabUser
        #self.tableWidget_2.setColumnHidden(4, True)
        self.btn = btn
        self.type = type
        #Backend
        self.db = Database()
        config_object = ConfigParser()
        config_object.read("config.ini")
        userInfo = config_object["USERINFO"]
        self.LOGGED_USER_ID = userInfo["LOGGED_USER_ID"]
        
        #Display tables
        self.loadData()
        self.btn.clicked.connect(self.exportCSV)

    def loadData(self):
        """This function loads data from an SQL database in the "Corps" user interface.
        Usage:
        -----------
            ui = Ui_Corps()
            ui.loadData()
        Return:
        -----------
            None
        Raises:
        -----------
            ConnectionError: If there is a problem connecting to the SQL database.
            DataLoadError: If there is an error during the data loading process.
        """
        try:
            conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                   database=self.db.DB_NAME)
            cursor = conn.cursor()
            sql_query = """SELECT 
                            Object, Type_object, Location, CAST(Calibration as char), CAST(Quantity as char), Category
                        FROM 
                            fakegcino.object_dist
                        ORDER BY
                            Object
                        """
            cursor.execute(sql_query)
            myresult = cursor.fetchall()

            table_row = 0
            self.tableWidget.setRowCount(len(myresult))
            for row in myresult:
                self.tableWidget.setItem(table_row, 0, QTableWidgetItem(row[0]))
                self.tableWidget.setItem(table_row, 1, QTableWidgetItem(row[1]))
                self.tableWidget.setItem(table_row, 2, QTableWidgetItem(row[2]))
                self.tableWidget.setItem(table_row, 3, QTableWidgetItem(row[3]))
                self.tableWidget.setItem(table_row, 4, QTableWidgetItem(row[4]))
                self.tableWidget.setItem(table_row, 5, QTableWidgetItem(row[5]))
                table_row = table_row +1  

            conn2 = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                   database=self.db.DB_NAME
                                   )
            cursor2 = conn2.cursor()
            sql_query2 = """SELECT 
                                o.Object, o.Type_object, o.Location, CAST(o.Calibration as char),actions, CAST(o.Quantity as char), CONCAT_WS(" ", m.firstname, m.lastname),
                                CAST(o.operation_datetime as char), o.project_name
                            FROM 
                                fakegcino.historique as o
                            INNER JOIN
                                fakegcino.managers as m
                            ON
                                m.id = o.user_id
                            WHERE
                                o.Type_object="Consumable"  
                        """
            cursor2.execute(sql_query2)
            myresult2 = cursor2.fetchall()

            table_row2 = 0
            self.tableWidget_2.setRowCount(len(myresult2))
            for row in myresult2:
                self.tableWidget_2.setItem(table_row2, 0, QTableWidgetItem(row[0]))
                self.tableWidget_2.setItem(table_row2, 1, QTableWidgetItem(row[1]))
                self.tableWidget_2.setItem(table_row2, 2, QTableWidgetItem(row[2]))
                self.tableWidget_2.setItem(table_row2, 3, QTableWidgetItem(row[3]))
                self.tableWidget_2.setItem(table_row2, 4, QTableWidgetItem(row[4]))
                self.tableWidget_2.setItem(table_row2, 5, QTableWidgetItem(row[5]))
                self.tableWidget_2.setItem(table_row2, 6, QTableWidgetItem(row[6]))
                self.tableWidget_2.setItem(table_row2, 7, QTableWidgetItem(row[7]))
                self.tableWidget_2.setItem(table_row2, 8, QTableWidgetItem(row[8]))
                table_row2 = table_row2 +1

            conn3 = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME,
                                       password=self.db.DB_PASSWORD,
                                       database=self.db.DB_NAME
                                       )
            cursor3 = conn3.cursor()
            sql_query3 = """SELECT 
                            Object, location , workshop, CAST(calibration as char), CAST(battery as char)
                        FROM 
                            fakegcino.object_loc
                        """
            cursor3.execute(sql_query3)
            myresult3 = cursor3.fetchall()

            table_row3 = 0
            self.tableWidget_3.setRowCount(len(myresult3))
            for row in myresult3:
                self.tableWidget_3.setItem(table_row3, 0, QTableWidgetItem(row[0]))
                self.tableWidget_3.setItem(table_row3, 1, QTableWidgetItem(row[1]))
                self.tableWidget_3.setItem(table_row3, 2, QTableWidgetItem(row[2]))
                self.tableWidget_3.setItem(table_row3, 3, QTableWidgetItem(row[3]))
                self.tableWidget_3.setItem(table_row3, 4, QTableWidgetItem(row[4]))
                table_row3 = table_row3 + 1

            conn4 = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                   database=self.db.DB_NAME)
            cursor4 = conn4.cursor()
            sql_query4 = f"""SELECT 
                            orders, status
                        FROM 
                            fakegcino.orders
                        WHERE user_id = '{self.LOGGED_USER_ID}'
                        """
            cursor4.execute(sql_query4)
            myresult4 = cursor4.fetchall()

            table_row4 = 0
            self.tab_user.setRowCount(len(myresult4))
            for row in myresult4:
                status_item = QTableWidgetItem(row[1])
                if status_item.text() == "Approuved":
                    status_item.setForeground(QColor("green"))
                elif status_item.text() == "Declined":
                    status_item.setForeground(QColor("red"))
                elif status_item.text() == "Pending":
                    status_item.setForeground(QColor("orange"))
                elif status_item.text() == "Cancled":
                    status_item.setForeground(QColor("grey"))
                else:
                    status_item.setForeground(QColor("black"))

                self.tab_user.setItem(table_row4, 0, QTableWidgetItem(row[0]))
                self.tab_user.setItem(table_row4, 1, status_item)
                table_row4 = table_row4 +1
        except Exception as e:
            print("Error while connecting to MySQL",e)

        return self.tableWidget, self.tableWidget_2, self.tableWidget_3

    def exportCSV(self):
        now = datetime.now()
        date_time = now.strftime("%Y_%m_%d")
        conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                database=self.db.DB_NAME)
        mycursor = conn.cursor()
        query = f"SELECT name FROM managers WHERE id = {self.LOGGED_USER_ID}"
        mycursor.execute(query)
        data = mycursor.fetchone()
        name = data[0]

        file_path = os.path.dirname(os.path.dirname(__file__)) + '/run/tendency' + '/' + str(date_time) + '_tendency_'+ name+ '.csv' 
        file_path = file_path.replace('\\', '/')
        file_path = os.path.normpath(file_path)

        if file_path:
            try:
                with open(file_path, mode="w", newline="") as file:
                    writer = csv.writer(file)
                    for row in range(self.tableWidget_2.rowCount()):
                        row_data = []
                        for column in range(self.tableWidget_2.columnCount()):
                            item = self.tableWidget_2.item(row, column)
                            if item is not None:
                                row_data.append(item.text())
                            else:
                                row_data.append("")
                        writer.writerow(row_data)

                QMessageBox.information(self, "CSV Exported", f"CSV file has been exported to:\n{file_path}")
            except IOError:
                QMessageBox.critical(self, "Error", "An error occurred while exporting the CSV file.")
        else:
            QMessageBox.warning(self, "Warning", "No file selected for export.")
            
class gcinotree(QDialog):
    def __init__(self, treeWidget, treeWidget_2):
        """
        """
        super(gcinotree, self).__init__()
        self.treeWidget = treeWidget
        self.treeWidget_2 = treeWidget_2
        self.treeWidget_2.hide()
        #Backend
        self.db = Database()
        config_object = ConfigParser()
        self.path_to_config =  "config.ini"
        config_object.read(self.path_to_config)
        userInfo = config_object["USERINFO"]
        self.LOGGED_USER_ID = userInfo["LOGGED_USER_ID"]
        self.groupTreeItems()
        self.groupTreeLocationItems()

    def groupTreeItems(self):
        """
        """
        try:
            conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                   database=self.db.DB_NAME)
            cursor = conn.cursor()
            sql_query = """SELECT 
                                DISTINCT Category,Type_object, Object 
                            FROM 
                                object_dist
                            ORDER BY 
                                Category, Type_object
                        """
            self.treeWidget.clear()
            cursor.execute(sql_query)
            results = cursor.fetchall()
            parent_items = {}
            for row in results:
                category = row[0]
                type_object = row[1]
                obj = row[2]
                if category in parent_items:
                    parent_item = parent_items[category]
                else:
                    parent_item = QTreeWidgetItem(self.treeWidget, [category])
                    parent_items[category] = parent_item
                child_items = [parent_item.child(i) for i in range(parent_item.childCount())]
                child_item = next((item for item in child_items if item.text(0) == type_object), None)
                if child_item is None:
                    child_item = QTreeWidgetItem(parent_item, [type_object])
                QTreeWidgetItem(child_item, [obj])
        except Exception as e:
            print("Error while connecting to MySQL",e)

    def groupTreeLocationItems(self):
        """
        """
        try:
            conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                   database=self.db.DB_NAME)
            cursor = conn.cursor()
            sql_query = """SELECT 
                                DISTINCT Location,workshop, storage_area 
                            FROM 
                                object_dist
                            ORDER BY 
                                Location, workshop
                        """
            self.treeWidget_2.clear()
            cursor.execute(sql_query)
            results = cursor.fetchall()
            parent_items = {}
            for row in results:
                category = row[0]
                type_object = row[1]
                obj = row[2]
                if category in parent_items:
                    parent_item = parent_items[category]
                else:
                    parent_item = QTreeWidgetItem(self.treeWidget_2, [category])
                    parent_items[category] = parent_item
                child_items = [parent_item.child(i) for i in range(parent_item.childCount())]
                child_item = next((item for item in child_items if item.text(0) == type_object), None)
                if child_item is None:
                    child_item = QTreeWidgetItem(parent_item, [type_object])
                QTreeWidgetItem(child_item, [obj])
        except Exception as e:
            print("Error while connecting to MySQL",e)


class gcinobox(QDialog):
    def __init__(self, Box, query, type):
        """
        """
        super(gcinobox, self).__init__()
        self.Box = Box
        self.query = query
        self.type = type

        self.db = Database()
        config_object = ConfigParser()
        config_object.read("config.ini")
        userInfo = config_object["USERINFO"]
        self.LOGGED_USER_ID = userInfo["LOGGED_USER_ID"]

        self.loadBox()

    def loadBox(self):
        """
        """
        conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                   database=self.db.DB_NAME)
        cursor = conn.cursor()
        cursor.execute(self.query)
        data = cursor.fetchall()
        if (self.type == "all"):
            self.Box.addItem("All")
        else:
            pass
        for i in data :
            var = str(i[0])
            self.Box.addItem(var)

class gcinoorders(QDialog):
    def __init__(self, send_btn, request, name, description, quantity, cout, table_user, count_label, table_warehouseman, table_manager):
        """
        """
        super(gcinoorders, self).__init__()
        # UI components 
        self.send_btn = send_btn
        self.request = request
        self.name = name
        self.description = description
        self.quantity = quantity
        self.cout = cout
        self.table = table_user
        self.table.setColumnWidth(0,325)
        self.table.setColumnWidth(1,325)
        self.count_label = count_label
        self.table2 = table_warehouseman
        self.table2.setColumnWidth(0,100)
        self.table2.setColumnWidth(1,200)
        self.table2.setColumnWidth(2,200)
        self.table2.setColumnWidth(3,200)
        self.table2.setColumnWidth(4,100)
        self.table2.setColumnWidth(5,100)
        self.table2.setColumnWidth(6,150)
        self.table3 = table_manager
        self.table3.setColumnWidth(0,500)

        #Connect to Database
        self.db = Database()
        config_object = ConfigParser()
        config_object.read("config.ini")
        userInfo = config_object["USERINFO"]
        self.LOGGED_USER_ID = userInfo["LOGGED_USER_ID"]
        self.LOGGED_USER_ROLE = userInfo["LOGGED_USER_ROLE"]

        #Connect to the e-mail (SMTP connection)
        self.config = configparser.ConfigParser()
        self.config.read('orders_config.ini')
        self.smtp_server = self.config['Server']['smtp_server']
        self.smtp_port = int(self.config['Server']['smtp_port'])
        self.sender_mail = self.config['User']['email']
        self.password = self.config['User']['password']
        self.receiver_mail = self.config['User']['receiver_email']

        #Local events
        self.description.textChanged.connect(self.updateCharactersCount)
        self.send_btn.clicked.connect(self.insertIntoOrderDB)
        self.send_btn.clicked.connect(self.addOrder)
        self.send_btn.clicked.connect(self.fillOrdersTable)
        self.fillOrdersTable()
        self.fillPurchasesTable()
        self.table3.cellClicked.connect(self.openBordoreauExcel)

    def sendRequest(self):
        """
        """
        msg = MIMEMultipart()
        msg['From'] = self.sender_mail
        msg['To'] = self.receiver_mail
        msg['Subject'] = str(self.request.text()) + ' - ' + str(self.name.text())
        msg.attach(MIMEText(str(self.description.toPlainText())))
        
        # Établir la connexion SMTP
        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.sender_mail, self.password)
        server.sendmail(self.sender_mail, self.receiver_mail, msg.as_string())
        server.quit()

    def generateOrderID(self):
        """
        """
        try:
            conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                    database=self.db.DB_NAME)
            mycursor = conn.cursor()
            random_id = "C" + ''.join([str(random.randint(0, 9)) for _ in range(7)])
            query_select = """SELECT orderID from orders"""
            mycursor.execute(query_select)
            data = mycursor.fetchall()
            for i in data:
                order_id = i[0]
                if (order_id == random_id):
                    random_id = "O"+ ''.join([str(random.randint(0, 9)) for _ in range(7)])
                else:
                    pass
        except Exception as e:
            QMessageBox.about(self, "Warning", str(e))
        return random_id
    
    def updateCharactersCount(self):
        """
        """
        char_count = len(self.description.toPlainText())
        self.count_label.setText(f"{char_count}/1000")
        if char_count >= 1000:
            self.count_label.setStyleSheet("color: red;")
            QMessageBox.about(self, "error", "Not valid Description")
        else:
            self.count_label.setStyleSheet("color: black;")
    
    def clearContents(self):
        """
        """
        self.description.clear()
        self.name.clear()
        self.request.clear()

    def addOrder(self):
        """
        """
        request_text = str(self.request.text())
        try:
            conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                    database=self.db.DB_NAME)
            mycursor = conn.cursor()
            query_select = """SELECT orders, status from orders where user_id =%s"""%(self.LOGGED_USER_ID)
            mycursor.execute(query_select)
            data = mycursor.fetchall()
            for i in data:
                request_id = i[0]
            conn.commit()
            self.close()
            if request_text:
                row_position = self.table.rowCount() 
                self.table.insertRow(row_position)
                self.table.setItem(row_position, 0, QTableWidgetItem(request_id))
                status_item = QTableWidgetItem("Pending")
                status_item.setForeground(QColor("orange"))
                self.table.setItem(row_position, 1, status_item)
        except Exception as e:
            QMessageBox.about(self, "Warning", str(e))

    def insertIntoOrderDB(self):
        """
        """
        request_text = str(self.request.text())
        name_text = str(self.name.text())
        descrip_text = str(self.description.toPlainText())
        quantity_text = str(self.quantity.text())
        cout_text = str(self.cout.text())
        random_id = self.generateOrderID()
        try:
            conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                    database=self.db.DB_NAME)
            mycursor = conn.cursor()
            query_insert = """INSERT INTO orders(orderID, orders, object, user_id, description, quantity, price, status) VALUES ('%s', '%s', '%s', %s, "%s", %s, %s, '%s')"""%(random_id, request_text, name_text, self.LOGGED_USER_ID, descrip_text, int(quantity_text), float(cout_text),"Pending")
            mycursor.execute(query_insert)
            conn.commit()
            self.close()
        except Exception as e:
            QMessageBox.about(self, "Warning", str(e))

    def acceptClicked(self, row, cond='clicked'):
        """
        """
        #MessageBox information
        self.table2.removeCellWidget(row, 5) 
        if cond != 'clicked': 
            pass
        else:
            QMessageBox.information(self, "Accept", "Accepted")

        #Update QTableWidget
        mod_icon = QIcon("./pen.png")
        mod_button = QPushButton()
        mod_button.setCursor(Qt.CursorShape.PointingHandCursor)
        mod_button.setIcon(mod_icon)
        mod_button.setFixedSize(20, 20)
        mod_button.clicked.connect(lambda _, row=row: self.modifyClicked(row))
        mod_button.clicked.connect(self.fillOrderTableByUser)
        mod_layout = QHBoxLayout()
        mod_layout.addWidget(mod_button)
        mod_widget = QWidget()
        mod_widget.setLayout(mod_layout)
        status_item = QTableWidgetItem("Approuved")
        status_item.setForeground(QColor("green"))
        self.table2.setCellWidget(row, 5, mod_widget)
        self.table2.setItem(row, 4, status_item)
        self.designAddIcon(row)

        #Update Database
        try:
            conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                    database=self.db.DB_NAME)
            mycursor = conn.cursor()
            orderid = self.table2.item(row,0).text()
            
            query_update = "UPDATE orders SET status ='Approuved' Where orderID = '%s'" %(orderid)
            mycursor.execute(query_update)
            conn.commit()
            self.close()
        except Exception as e:
            QMessageBox.about(self, "Warning", str(e))

    def rejectClicked(self, row, cond='clicked'):
        self.table2.removeCellWidget(row, 5) 
        if cond =='clicked':
            QMessageBox.information(self, "Reject", "Rejected")
        else:
            pass
        
        #Update QTableWidget
        mod_icon = QIcon("./pen.png")
        mod_button = QPushButton()
        mod_button.setCursor(Qt.CursorShape.PointingHandCursor)
        mod_button.setIcon(mod_icon)
        mod_button.setFixedSize(20, 20)
        mod_button.clicked.connect(lambda _, row=row: self.modifyClicked(row))
        mod_button.clicked.connect(self.fillOrderTableByUser)
        mod_layout = QHBoxLayout()
        mod_layout.addWidget(mod_button)
        mod_widget = QWidget()
        mod_widget.setLayout(mod_layout)
        status_item = QTableWidgetItem("Declined")
        status_item.setForeground(QColor("red"))

        self.table2.setCellWidget(row, 5, mod_widget)
        self.table2.setItem(row, 4, status_item)

        #Update Database
        try:
            conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                    database=self.db.DB_NAME)
            mycursor = conn.cursor()
            orderid = self.table2.item(row,0).text()
            
            query_update = "UPDATE orders SET status ='Declined' Where orderID = '%s'" %(orderid)
            mycursor.execute(query_update)
            conn.commit()
            self.close()
        except Exception as e:
            QMessageBox.about(self, "Warning", str(e))

    def modifyClicked(self, row):
        """
        """
        accept_icon = QIcon("./accept.png")  # Replace with actual accept icon path
        refuse_icon = QIcon("./rejected.png")
        actions_layout = QHBoxLayout()
        accept_button = QPushButton()
        accept_button.setCursor(Qt.CursorShape.PointingHandCursor)
        accept_button.setIcon(accept_icon)
        accept_button.setFixedSize(20, 20)
        accept_button.clicked.connect(lambda _, row=row: self.acceptClicked(row))
        accept_button.clicked.connect(self.fillOrderTableByUser)

        refuse_button = QPushButton()
        refuse_button.setCursor(Qt.CursorShape.PointingHandCursor)
        refuse_button.setIcon(refuse_icon)
        refuse_button.setFixedSize(20, 20)
        refuse_button.clicked.connect(lambda _, row=row: self.rejectClicked(row))
        refuse_button.clicked.connect(self.fillOrderTableByUser)
        actions_layout.addWidget(accept_button)
        actions_layout.addWidget(refuse_button)
        actions_widget = QWidget()
        actions_widget.setLayout(actions_layout)
        status_item = QTableWidgetItem("Pending")
        status_item.setForeground(QColor("orange"))
                    
        self.table2.setItem(row, 4, status_item)
        self.table2.setCellWidget(row, 5, actions_widget)
        empty_item = QWidget()
        self.table2.setCellWidget(row,6, empty_item)

        #Update Database
        try:
            conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                    database=self.db.DB_NAME)
            mycursor = conn.cursor()
            orderid = self.table2.item(row,0).text()
            
            query_update = "UPDATE orders SET status ='Pending' Where orderID = '%s'" %(orderid)
            mycursor.execute(query_update)
            conn.commit()
            self.close()
        except Exception as e:
            QMessageBox.about(self, "Warning", str(e))
    
    def cancelClicked(self, row):
        """
        """
        cancel_icon = QIcon("./cancel.png") 
        cancel_layout = QHBoxLayout()
        cancel_button = QPushButton()
        cancel_button.setIcon(cancel_icon)
        cancel_button.setFixedSize(20, 20)
        cancel_layout.addWidget(cancel_button)
        cancel_widget = QWidget()
        cancel_widget.setLayout(cancel_layout)
        self.table2.setItem(row, 4, QTableWidgetItem("Canceled"))
        self.table2.setCellWidget(row, 5, cancel_widget)
    
    def confirmClicked(self, row):
        """
        """
        cancel_widget = QWidget()
        self.table2.setItem(row, 4, QTableWidgetItem("Confirmed"))
        self.table2.setCellWidget(row, 5, cancel_widget)

    def designAddIcon(self, row):
        """
        """
        add_icon = QIcon("./add.png") 
        add_layout = QHBoxLayout()
        add_button = QPushButton()
        add_button.setIcon(add_icon)
        add_button.setFixedSize(20, 20)
        add_layout.addWidget(add_button)
        add_widget = QWidget()
        add_widget.setLayout(add_layout)
        self.table2.setCellWidget(row, 6, add_widget)

    def fillOrderTableByUser(self):
        """
        """
        self.table.clearContents()
        try:
            conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                    database=self.db.DB_NAME)
            mycursor = conn.cursor()
            query_select = """SELECT 
                                o.orders, o.status
                            FROM
                                orders o
                            WHERE 
                                user_id =%s
                            ORDER BY
                                o.status DESC
                           """ %(self.LOGGED_USER_ID)
            mycursor.execute(query_select)
            data = mycursor.fetchall()
            table_row = 0
            self.table.setRowCount(len(data))
            for row in data:
                self.table.setItem(table_row, 0, QTableWidgetItem(row[0]))
                status_item = QTableWidgetItem(row[1])
                if status_item.text() == "Pending":
                    status_item.setForeground(QColor("orange"))
                elif status_item.text() == "Approuved":
                    status_item.setForeground(QColor("green"))
                elif status_item.text() == "Declined":
                    status_item.setForeground(QColor("red"))
                else:
                    status_item.setForeground(QColor("grey"))
                self.table.setItem(table_row, 1, status_item)
                table_row = table_row+1
        except Exception as e:
            QMessageBox.about(self, "Warning", str(e))

    def fillOrdersTable(self):
        """
        """
        try:
            conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                    database=self.db.DB_NAME)
            mycursor = conn.cursor()
            query_select = """SELECT 
                                o.orderID, o.orders, o.object, m.name, o.status
                              FROM
                                orders o
                              INNER JOIN
                                managers m
                              ON
                                m.id = o.user_id
                           """
            mycursor.execute(query_select)
            data = mycursor.fetchall()
            table_row = 0
            self.table2.setRowCount(len(data))
            accept_icon = QIcon("./accept.png")  
            refuse_icon = QIcon("./rejected.png")
            
            for row in data:
                self.table2.setItem(table_row, 0, QTableWidgetItem(row[0]))
                self.table2.setItem(table_row, 1, QTableWidgetItem(row[1]))
                self.table2.setItem(table_row, 2, QTableWidgetItem(row[2]))
                self.table2.setItem(table_row, 3, QTableWidgetItem(row[3]))
                status_item = QTableWidgetItem(row[4])
                status_item.setForeground(QColor("orange"))
                self.table2.setItem(table_row, 4, status_item)
                if self.table2.item(table_row, 4).text() == "Pending":
                    actions_layout = QHBoxLayout()
                    accept_button = QPushButton()
                    accept_button.setCursor(Qt.CursorShape.PointingHandCursor)
                    accept_button.setIcon(accept_icon)
                    accept_button.setFixedSize(20, 20)
                    accept_button.clicked.connect(lambda _, row=table_row: self.acceptClicked(row))
                    accept_button.clicked.connect(self.fillOrderTableByUser)

                    refuse_button = QPushButton()
                    refuse_button.setCursor(Qt.CursorShape.PointingHandCursor)
                    refuse_button.setIcon(refuse_icon)
                    refuse_button.setFixedSize(20, 20)
                    refuse_button.clicked.connect(lambda _, row=table_row: self.rejectClicked(row))
                    refuse_button.clicked.connect(self.fillOrderTableByUser)

                    actions_layout.addWidget(accept_button)
                    actions_layout.addWidget(refuse_button)
                    actions_widget = QWidget()
                    actions_widget.setLayout(actions_layout)
                    self.table2.setCellWidget(table_row, 5, actions_widget)
                elif self.table2.item(table_row, 4).text() == "Declined":
                    self.rejectClicked(table_row, cond='NoClicked')
                elif self.table2.item(table_row, 4).text() == "Approuved":
                    self.acceptClicked(table_row, cond='NoClicked')
                    self.designAddIcon(table_row)
                elif self.table2.item(table_row,4).text() == "Confirmed":
                    self.confirmClicked(table_row)
                else:
                    self.cancelClicked(table_row)
                table_row = table_row +1  

        except Exception as e:
            QMessageBox.about(self, "Warning", str(e))
    
    def confirmPurchases(self, row, excel_file, action="accept"):
        """
        """
        now = datetime.now()
        now = now.strftime("%Y_%m_%d")
        if action == "accept":
            self.table3.removeCellWidget(row, 1)
            self.table3.setItem(row,1, QTableWidgetItem('Confirmed'))
            shutil.move('./Bordoreau/' + excel_file, './Purchases/Confirmed/'+ str(now)+ '_' + excel_file)
        else:
            self.table3.removeCellWidget(row, 1)
            self.table3.setItem(row,1, QTableWidgetItem('Declined'))
            shutil.move('./Bordoreau/' + excel_file, './Purchases/Declined/'+ str(now) + '_' + excel_file)

    def fillPurchasesTable(self):
        """
        """
        directory_path = "./Bordoreau/" 
        excel_files = [f for f in os.listdir(directory_path) if f.endswith(".xlsx")]
        self.table3.setRowCount(len(excel_files))  # Nombre de lignes

        for row, excel_file in enumerate(excel_files):
            item = QTableWidgetItem(excel_file)
            self.table3.setItem(row, 0, item)

            accept_icon = QIcon("./accept.png")  # Replace with actual accept icon path
            refuse_icon = QIcon("./rejected.png")
            actions_layout = QHBoxLayout()
            accept_button = QPushButton()
            accept_button.setCursor(Qt.CursorShape.PointingHandCursor)
            accept_button.setIcon(accept_icon)
            accept_button.setFixedSize(20, 20)
            accept_button.clicked.connect(lambda _,excel_file=excel_file, row=row: self.confirmPurchases(row, excel_file, action='accept'))
        
            refuse_button = QPushButton()
            refuse_button.setCursor(Qt.CursorShape.PointingHandCursor)
            refuse_button.setIcon(refuse_icon)
            refuse_button.setFixedSize(20, 20)
            refuse_button.clicked.connect(lambda _,excel_file=excel_file, row=row: self.confirmPurchases(row, excel_file, action='refuse'))
            actions_layout.addWidget(accept_button)
            actions_layout.addWidget(refuse_button)
            actions_widget = QWidget()
            actions_widget.setLayout(actions_layout)
            self.table3.setCellWidget(row, 1, actions_widget)

    def openBordoreauExcel(self, row, col):
        """
        """
        excel_exe = r'C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE'
        if col == 0:  # Colonne des noms de fichiers
            file_name = self.table3.item(row, col).text()
            file_path = os.path.join('./Bordoreau', file_name)
            
            if os.path.exists(file_path):
                subprocess.run(f'start "" "{excel_exe}" "{file_path}"', shell=True)
            else:
                print(f"The file {file_path} does not exist!")

