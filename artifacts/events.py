# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
from forms import insertform, profileform, tendency, projectform, bordoreauform
from PyQt6.QtWidgets import QDialog, QTableWidgetItem, QMessageBox, QComboBox, QPushButton
import threading

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
    def __init__(self, Box, table, table2, table3, col_name, treeWidget, treeWidget_2, search, calendar, type):
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
        self.table3 = table3
        self.search = search
        self.search.setPlaceholderText("Search...")
        self.type = type
        self.calendar = calendar
        self.calendar.setVisible(False)
        self.start_date = None
        self.end_date = None

        self.db = Database()
        config_object = ConfigParser()
        self.path_to_config ="config.ini"
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
        return query
    
    def filterCalendar(self, from_box=False):
        query = self.filterBox()
        selected_date = self.calendar.selectedDate()
        if not self.start_date:
            self.start_date = selected_date
            query += f" AND date(operation_datetime) = '{selected_date.toString('yyyy-MM-dd')}'"
            
        elif not self.end_date:
            self.end_date = selected_date
            query += f" AND date(operation_datetime) >= '{self.start_date.toString('yyyy-MM-dd')}' AND date(operation_datetime) <= '{selected_date.toString('yyyy-MM-dd')}'"
        else:
            self.start_date = selected_date
            self.end_date = None
            query += f" AND date(operation_datetime) = '{selected_date.toString('yyyy-MM-dd')}'"
        conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                        database=self.db.DB_NAME)
        
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
        mod_tree = gcinotree(self.tree_widget, self.tree_widget2)
        btn = QPushButton()
        box = QComboBox()
        mod_hist = gcinotables(self.table2, self.table, self.table3, btn, box)

class localisation():

    def __init__(self, table):
        """
        """
        super(localisation, self).__init__()
        self.selected_object = None
        self.table = table
        self.table.cellClicked.connect(self.cellClicked)  # Connectez le signal cellClicked à la fonction

        self.db = Database()

        config_object = ConfigParser()
        self.path_to_config = "config.ini"
        config_object.read(self.path_to_config)
        userInfo = config_object["USERINFO"]
        self.LOGGED_USER_ID = userInfo["LOGGED_USER_ID"]

    def cellClicked(self, row, col):
        if col == 0:
            item = self.table.item(row, col)
            if item:
                self.selected_object = item.text()
                print("Objet sélectionné :", self.selected_object)

    def activateLED(self):
        if self.selected_object is not None:
            update_on_query = f"UPDATE object_loc SET LED = 1 WHERE Object = '{self.selected_object}'"
            update_off_query = f"UPDATE object_loc SET LED = 0 WHERE Object = '{self.selected_object}'"

            def update_led_on():
                conn = None
                cursor = None
                try:
                    conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                              database=self.db.DB_NAME)
                    cursor = conn.cursor()

                    cursor.execute(update_on_query)
                    conn.commit()
                    print("LED activée avec succès pour l'objet :", self.selected_object)

                    # Planifier la mise hors tension après 10 secondes
                    threading.Timer(20, update_led_off).start()

                except Exception as e:
                    print("Erreur lors de l'activation de la LED :", str(e))

                finally:
                    if cursor:
                        cursor.close()
                    if conn:
                        conn.close()

            def update_led_off():
                conn = None
                cursor = None
                try:
                    conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                              database=self.db.DB_NAME)
                    cursor = conn.cursor()

                    cursor.execute(update_off_query)
                    conn.commit()
                    print("LED désactivée avec succès pour l'objet :", self.selected_object)

                except Exception as e:
                    print("Erreur lors de la désactivation de la LED :", str(e))

                finally:
                    if cursor:
                        cursor.close()
                    if conn:
                        conn.close()

            # Lancer le processus d'activation
            update_led_on()

        else:
            print("Aucun objet sélectionné.")

    def activateBUZZER(self):
        if self.selected_object is not None:
            update_on_query = f"UPDATE object_loc SET Buzzer = 1 WHERE Object = '{self.selected_object}'"
            update_off_query = f"UPDATE object_loc SET Buzzer = 0 WHERE Object = '{self.selected_object}'"

            def update_buzzer_on():
                conn = None
                cursor = None
                try:
                    conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                              database=self.db.DB_NAME)
                    cursor = conn.cursor()

                    cursor.execute(update_on_query)
                    conn.commit()
                    print("Buzzer activée avec succès pour l'objet :", self.selected_object)

                    # Planifier la mise hors tension après 10 secondes
                    threading.Timer(20, update_buzzer_off).start()

                except Exception as e:
                    print("Erreur lors de l'activation de la Buzzer :", str(e))

                finally:
                    if cursor:
                        cursor.close()
                    if conn:
                        conn.close()

            def update_buzzer_off():
                conn = None
                cursor = None
                try:
                    conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                              database=self.db.DB_NAME)
                    cursor = conn.cursor()

                    cursor.execute(update_off_query)
                    conn.commit()
                    print("Buzzer désactivée avec succès pour l'objet :", self.selected_object)

                except Exception as e:
                    print("Erreur lors de la désactivation de la Buzzer :", str(e))

                finally:
                    if cursor:
                        cursor.close()
                    if conn:
                        conn.close()

            # Lancer le processus d'activation
            update_buzzer_on()

        else:
            print("Aucun objet sélectionné.")
