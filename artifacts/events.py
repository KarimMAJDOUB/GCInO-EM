# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
from forms import insertform, profileform, plotactiv
from PyQt6.QtWidgets import QDialog, QTableWidgetItem
from PyQt6.uic import loadUi
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

    def openPlotForm(self):
        """
        """
        plotactiv().exec()


class filterevents(QDialog):
    def __init__(self,Box,table,table2,col_name,treeWidget):
        """
        """
        super(filterevents, self).__init__()
        self.Box = Box
        self.table = table
        self.col_name = col_name
        self.tree_widget = treeWidget
        self.table2 = table2
        self.table2.setColumnHidden(5, True)

        self.db = Database()
        config_object = ConfigParser()
        self.path_to_config = os.path.dirname(os.path.dirname(__file__)) + "\system_files\config.ini"
        config_object.read(self.path_to_config)
        userInfo = config_object["USERINFO"]
        self.LOGGED_USER_ID = userInfo["LOGGED_USER_ID"]

    def filterBox(self):
        filters = {}
        for i, combo_box in enumerate(self.Box):
            filter_option = combo_box.currentText()
            if filter_option != "All":
                filters[self.col_name[i]] = filter_option
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

    def filterTree(self):
        selected_items = self.tree_widget.selectedItems()
        selected_item = selected_items[0].text(0)

        if not selected_item:
            # If no items are selected, show all data
            for row in range(self.table2.rowCount()):
                self.table2.showRow(row)
            return
        
        if selected_items[0].parent() is None: 
            for row in range(self.table2.rowCount()):
                if selected_item == self.table2.item(row,5).text():
                    self.table2.showRow(row)
                else:
                    self.table2.hideRow(row)

        if selected_items[0].child(0) is None: 
            for row in range(self.table2.rowCount()):
                if selected_item == self.table2.item(row,0).text():
                    self.table2.showRow(row)
                else:
                    self.table2.hideRow(row)

        if selected_items[0].parent() is not None and selected_items[0].child(0) is not None:
            parent_item = selected_items[0].parent().text(0)
            child_item = [selected_items[0].child(i).text(0) for i in range(selected_items[0].childCount())]
            for row in range(self.table2.rowCount()):
                if parent_item == self.table2.item(row,5).text() and  self.table2.item(row,0).text() in child_item and selected_item == self.table2.item(row,1).text():
                    self.table2.showRow(row)     
                else:
                    self.table2.hideRow(row)

    def populate_table(self, data):
        self.table2.clearContents()
        self.table2.setRowCount(len(data))
        self.table2.setColumnCount(len(data[0]))

        for row in range(len(data)):
            for col in range(len(data[0])):
                item = QTableWidgetItem(data[row][col])
                self.table2.setItem(row, col, item)

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
        
        self.populate_table(initial_data)