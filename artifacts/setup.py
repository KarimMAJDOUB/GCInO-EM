# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QDialog, QTreeWidgetItem, QMainWindow, QWidget, QTableWidgetItem, QMessageBox, QDialog, QFileDialog
from database import Database
from configparser import ConfigParser
import pymysql.connections as MySQLdb
import csv 
from datetime import datetime

class gcinodesign(QDialog):
    def __init__(self, table, table2, tab):
        """
        """
        super(gcinodesign, self).__init__()
        self.table = table
        self.table2 = table2
        self.tab = tab
        #Backend
        self.db = Database()
        config_object = ConfigParser()
        self.path_to_config = os.path.dirname(os.path.dirname(__file__)) + "\system_files\config.ini"
        config_object.read("config.ini")
        userInfo = config_object["USERINFO"]
        self.LOGGED_USER_ID = userInfo["LOGGED_USER_ID"]
        self.LOGGED_USER_ROLE = userInfo["LOGGED_USER_ROLE"]

        self.designTables()
        self.disableTab(self.tab)

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



class gcinotables(QMainWindow):
    def __init__(self, tableWidget, tableWidget2, btn, type):
        """
        """
        super(gcinotables, self).__init__()
        self.tableWidget = tableWidget
        self.tableWidget_2 = tableWidget2
        self.tableWidget_2.setColumnHidden(4, True)
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
                                fakegcino.object_dist as o
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
        except Exception as e:
            print("Error while connecting to MySQL",e)

        return self.tableWidget, self.tableWidget_2

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
        self.path_to_config = os.path.dirname(os.path.dirname(__file__)) + "\system_files\config.ini"
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