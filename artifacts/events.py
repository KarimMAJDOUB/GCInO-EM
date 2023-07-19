# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
from forms import insertform, profileform, tendency, projectform
from PyQt6.QtWidgets import QDialog, QTableWidgetItem
from database import Database
from configparser import ConfigParser
import pymysql.connections as MySQLdb

class eventshandler(QDialog):
    def __init__(self):
        """
        """
    
    def openInsertionForm(self):
        """
        """
        insertform().exec()

    def openProfileForm(self):
        """
        """
        profileform().exec()
    
    def openProjForm(self):
        """
        """
        projectform().exec()

    def openPlotForm(self):
        """
        """
        tendency().exec()

class filterevents(QDialog):
    def __init__(self, Box, table, table2, col_name, treeWidget, type):
        """
        """
        super(filterevents, self).__init__()
        self.Box = Box
        self.table = table
        self.col_name = col_name
        self.tree_widget = treeWidget
        self.table2 = table2
        self.type = type
        self.table2.setColumnHidden(5, True)
        self.Box[3].setEnabled(False)
        
        self.db = Database()
        config_object = ConfigParser()
        self.path_to_config = os.path.dirname(os.path.dirname(__file__)) + "\system_files\config.ini"
        config_object.read(self.path_to_config)
        userInfo = config_object["USERINFO"]
        self.LOGGED_USER_ID = userInfo["LOGGED_USER_ID"]

    def filterBox(self):
        """
        """
        filters = {}
        for i, combo_box in enumerate(self.Box):
            filter_option = combo_box.currentText()
            if filter_option != "All":
                filters[self.col_name[i]] = filter_option
            if filter_option == "Consumable":
                self.table.setColumnHidden(4, True)
                self.Box[3].setEnabled(False)
            elif filter_option == "Tooling":
                self.table.setColumnHidden(4, False)
                self.Box[3].setEnabled(True)

        conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                        database=self.db.DB_NAME)
        query = """SELECT 
                        o.Object, o.Type_object, o.Location, CAST(o.Calibration as char),actions, CAST(o.Quantity as char), m.name,
                        CAST(o.operation_datetime as char), o.project_name
                    FROM 
                        fakegcino.object_dist as o
                    INNER JOIN
                        fakegcino.managers as m
                    ON
                        m.id = o.user_id
                    WHERE 
                        1=1"""
        for filter_name, filter_value in filters.items():
                query += f" AND {filter_name} = '{filter_value}'"

        with conn.cursor() as cursor:
            cursor.execute(query)
            result = cursor.fetchall()
            self.table.setRowCount(len(result))
            for row_idx, row in enumerate(result):
                for col_idx, col_value in enumerate(row):
                    item = QTableWidgetItem(str(col_value))
                    self.table.setItem(row_idx, col_idx, item)
            
    def populateTable(self, data):
        """
        """
        self.table2.clearContents()
        self.table2.setRowCount(len(data))
        self.table2.setColumnCount(len(data[0]))

        for row in range(len(data)):
            for col in range(len(data[0])):
                item = QTableWidgetItem(data[row][col])
                self.table2.setItem(row, col, item)

    def filterTree(self):
        """
        """
        selected_items = self.tree_widget.selectedItems()
        selected_item = selected_items[0].text(0)
        conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                   database=self.db.DB_NAME)
        query = "SELECT Object, Type_Object, Location, CAST(Calibration as char), CAST(Quantity as char), Category FROM fakegcino.object_dist"

        if not selected_item:
            # If no items are selected, show all data
            for row in range(self.table2.rowCount()):
                self.table2.showRow(row)
            return
        if selected_items[0].parent() is None: 
            query += f" WHERE Category = '{selected_item}'"
        elif selected_items[0].child(0) is None: 
            query += f" WHERE Category = '{selected_items[0].parent().parent().text(0)}' AND Type_Object = '{selected_items[0].parent().text(0)}' AND Object = '{selected_item}'"
        elif selected_items[0].parent() is not None and selected_items[0].child(0) is not None:
            query += f" WHERE Type_Object = '{selected_item}' AND  Category= '{selected_items[0].parent().text(0)}'"
        else:
            pass

        if query:
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            self.populateTable(result)

    def resetTable(self):
        # Clear any selection in the tree view
        self.tree_widget.clearSelection()

        # Reset the table with initial data
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
        initial_data = list(myresult)
        self.populateTable(initial_data)