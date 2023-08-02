# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
from forms import insertform, profileform, tendency, projectform, modifyform
from PyQt6.QtWidgets import QDialog, QTableWidget, QTableWidgetItem, QMessageBox, QComboBox, QPushButton
import sys
from PyQt6.uic import loadUi

from database import Database
from configparser import ConfigParser
import pymysql.connections as MySQLdb
from setup import gcinotree, gcinotables

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
    def __init__(self, Box, table, table2, col_name, treeWidget, treeWidget_2, search, type):
        """
        """
        super(filterevents, self).__init__()
        self.Box = Box
        self.table = table
        self.col_name = col_name
        self.tree_widget = treeWidget
        self.tree_widget2 = treeWidget_2
        self.table2 = table2
        self.table2.setColumnHidden(5, True)
        self.search = search
        self.search.setPlaceholderText("Search...")
        self.type = type
        
        self.db = Database()
        config_object = ConfigParser()
        self.path_to_config = os.path.dirname(os.path.dirname(__file__)) + "\system_files\config.ini"
        config_object.read(self.path_to_config)
        userInfo = config_object["USERINFO"]
        self.LOGGED_USER_ID = userInfo["LOGGED_USER_ID"]
        
        self.search.textChanged.connect(self.filterSearchBar)

    def filterBox(self):
        """
        """
        filters = {}
        for i, combo_box in enumerate(self.Box):
            filter_option = combo_box.currentText()
            if filter_option != "All":
                filters[self.col_name[i]] = filter_option
            if filter_option == "Consumable":
                #self.table.setColumnHidden(4, False)
                self.Box[3].setEnabled(True)
            elif filter_option == "Tooling":
                #self.table.setColumnHidden(4, False)
                self.Box[3].setEnabled(True)

        conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                        database=self.db.DB_NAME)
        query = """SELECT 
                        o.Object, o.Type_object, o.Location, CAST(o.Calibration as char),actions, CAST(o.Quantity as char), m.name,
                        CAST(o.operation_datetime as char), o.project_name
                    FROM 
                        fakegcino.historique as o
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
        try:
            self.table2.clearContents()
            self.table2.setRowCount(len(data))
            self.table2.setColumnCount(len(data[0]))
        except Exception as e:
                QMessageBox.about(self, "Error", "error : There are no data") 

        for row in range(len(data)):
            for col in range(len(data[0])):
                item = QTableWidgetItem(data[row][col])
                self.table2.setItem(row, col, item)

    def filterTree(self):
        """
        """
        self.tree_widget2.show()
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

        return query

    def filterLocationTree(self):
        """
        """
        selected_items = self.tree_widget2.selectedItems()
        selected_item = selected_items[0].text(0)
        conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                   database=self.db.DB_NAME)
        query = self.filterTree()

        if not selected_item:
            # If no items are selected, show all data
            for row in range(self.table2.rowCount()):
                self.table2.showRow(row)
            return
        if selected_items[0].parent() is None: 
            query += f" AND Location = '{selected_item}'"
        elif selected_items[0].child(0) is None: 
            query += f" AND Location = '{selected_items[0].parent().parent().text(0)}' AND workshop = '{selected_items[0].parent().text(0)}' AND storage_area = '{selected_item}'"
        elif selected_items[0].parent() is not None and selected_items[0].child(0) is not None:
            query += f" AND workshop = '{selected_item}' AND  Location= '{selected_items[0].parent().text(0)}'"
        else:
            pass

        if query:
            cursor = conn.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            self.populateTable(result)

    def filterSearchBar(self, text):
        if not text:
            self.showAll()
            return
        items = self.findItemsRecursive(self.tree_widget.invisibleRootItem(), text)
        items2 = self.findItemsRecursive(self.tree_widget2.invisibleRootItem(), text)
        self.hideAll()
        for item in items:
            self.showItemAndParents(item)
        for item2 in items2:
            self.showItemAndParents(item2)

    def findItemsRecursive(self, item, text):
        result = []
        for i in range(item.childCount()):
            child_item = item.child(i)
            if text.lower() in child_item.text(0).lower():
                result.append(child_item)
            result.extend(self.findItemsRecursive(child_item, text))
        return result

    def hideAll(self):
        root_item = self.tree_widget.invisibleRootItem()
        self.hideItemAndChildren(root_item)
        root_item2 = self.tree_widget2.invisibleRootItem()
        self.hideItemAndChildren(root_item2)

    def hideItemAndChildren(self, item):
        item.setHidden(True)
        for i in range(item.childCount()):
            child_item = item.child(i)
            self.hideItemAndChildren(child_item)

    def showAll(self):
        root_item = self.tree_widget.invisibleRootItem()
        self.showItemAndChildren(root_item)
        root_item2 = self.tree_widget2.invisibleRootItem()
        self.showItemAndChildren(root_item2)

    def showItemAndChildren(self, item):
        item.setHidden(False)
        for i in range(item.childCount()):
            child_item = item.child(i)
            self.showItemAndChildren(child_item)

    def showItemAndParents(self, item):
        item.setHidden(False)
        parent_item = item.parent()
        while parent_item is not None:
            parent_item.setHidden(False)
            parent_item = parent_item.parent()
            self.tree_widget.expandAll()
            self.tree_widget2.expandAll()


    def resetTable(self):
        # Clear any selection in the tree view
        self.tree_widget2.setVisible(False)
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

        mod_tree = gcinotree(self.tree_widget, self.tree_widget2)
        btn = QPushButton()
        box = QComboBox()
        mod_hist = gcinotables(self.table2, self.table, btn, box)