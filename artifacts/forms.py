# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
from datetime import datetime
import random

from PyQt6 import QtCore
from database import Database
from configparser import ConfigParser
import pymysql.connections as MySQLdb
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QMessageBox, QDialog, QVBoxLayout, QWidget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt

class insertform(QDialog):
    def __init__(self):
        """Initializes an instance of the insertfrom class.
        Usage:
        -----------
            c_insert = insertform()
        Return:
        -----------
            None
        """
        super(insertform, self).__init__()
        self.ui = loadUi(os.path.join(os.path.dirname(__file__), "Data_insertion.ui"), self)
        
        self.db = Database()
        config_object = ConfigParser()
        config_object.read("config.ini")
        userInfo = config_object["USERINFO"]
        self.LOGGED_USER_ID = userInfo["LOGGED_USER_ID"]
        
        self.ui.insertButton.clicked.connect(self.insertData)
        self.ui.cancelButton.clicked.connect(self.cancel)
        self.loadBox()

    def loadBox(self):
        """
        
        """
        ### Add list of project in comboBox
        conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                   database=self.db.DB_NAME)
        cursor = conn.cursor()
        query_project_select = f"SELECT projectname FROM projects p WHERE p.user_id='{self.LOGGED_USER_ID}'"
        query_action_select = f"SELECT Distinct actions FROM object_dist"
        query_category_select = f"SELECT Distinct Category FROM object_dist"
        cursor.execute(query_project_select)
        data_proj = cursor.fetchall()
        for i in data_proj : 
            res = i[0]
            self.projectBox.addItem(res)

        cursor2 = conn.cursor()
        cursor2.execute(query_action_select)
        data_action = cursor2.fetchall()
        for i in data_action : 
            res = i[0]
            self.actionBox.addItem(res)

        cursor3 = conn.cursor()
        cursor3.execute(query_category_select)
        data_cat = cursor3.fetchall()
        for i in data_cat : 
            res = i[0]
            self.categoryBox.addItem(res)

    def cancel(self):
        """This function allows the user to navigate back to the previous screen in the application.
        Usage:
        -----------
            ui = Ui_ForgetPassword()
            ui.goback()

        Return:
        -----------
            None
        """
        self.close()

    def insertData(self):
        """
        This function will insert a row of data in the object_dist table
        :return:
        """
        objectText      = str(self.objectText.text())
        typeText        = str(self.TypeBox.currentText())
        locationText    = str(self.locationText.text())
        calibrationText = str(self.calibrationText.text())
        quantityText    = str(self.quantityText.text())
        actionText      = str(self.actionBox.currentText())
        projectText     = str(self.projectBox.currentText())
        categoryText    = str(self.categoryBox.currentText())

        if(len(objectText.strip()) == 0 or len(calibrationText.strip()) == 0 or len(quantityText.strip()) == 0 or len(locationText.strip()) == 0 or len(typeText.strip()) == 0
            or len(projectText.strip()) == 0):
            msgBox = QMessageBox()
            msgBox.setText("All fields must be filled before confirming !")
            msgBox.setWindowTitle("Attention")
            msgBox.exec()
        else:
            now = datetime.now()
            date_time = now.strftime("%Y-%m-%d %H:%M:%S")
            conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                               database=self.db.DB_NAME)
            mycursor = conn.cursor()
            query_insert = "INSERT INTO object_dist(Object,Type_object,Location, Calibration, Quantity, Category,operation_datetime,user_id,actions,project_name) VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" %(objectText,typeText,locationText,calibrationText,quantityText,categoryText, date_time, self.LOGGED_USER_ID, actionText, projectText)
            mycursor.execute(query_insert)
            conn.commit()
            self.close()

class profileform(QDialog):
    def __init__(self):
        """Initializes an instance of the Ui_SignUp class.
        Usage:
        -----------
            ui = Ui_SignUp()
        Return:
        -----------
            None
        """
        super(profileform, self).__init__()
        loadUi(os.path.join(os.path.dirname(__file__), "profile.ui"), self)

        self.saveButton.clicked.connect(self.update_data)

        self.db = Database()
        config_object = ConfigParser()
        config_object.read("config.ini")
        userInfo = config_object["USERINFO"]
        self.LOGGED_USER_ID = userInfo["LOGGED_USER_ID"]

        try:
            conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                   database=self.db.DB_NAME)
            cursor = conn.cursor()
            query = f"SELECT username,email,firstname,lastname,ismanager, Society, Entity FROM managers WHERE id='{self.LOGGED_USER_ID}'"
            query_proj = f"SELECT projectname FROM projects p INNER JOIN managers m ON p.user_id = m.id  WHERE m.id='{self.LOGGED_USER_ID}'"
            cursor.execute(query)
            data = cursor.fetchone()
            cursor.execute(query_proj)
            data_proj = cursor.fetchall()
            self.usernameTextField.setText(data[0])
            self.emailTextField.setText(data[1])
            self.firstNameTextField.setText(data[2])
            self.lastNameTextField.setText(data[3])
            self.usernameTextField_2.setText(data[5])
            self.usernameTextField_3.setText(data[6])
            for i in data_proj : 
                res = i[0]
                self.comboBox.addItem(res)
            
            if(int(data[4]) == 0):
                self.usernameTextField.setEnabled(False)
                self.emailTextField.setEnabled(False)
                self.firstNameTextField.setEnabled(False)
                self.lastNameTextField.setEnabled(False)
                self.saveButton.setEnabled(False)
                self.usernameTextField_2.setEnabled(False)
                self.usernameTextField_3.setEnabled(False)
                #self.comboBox.setEnabled(False)
        except Exception as e:
            QMessageBox.about(str(e))

    def update_data(self):

        username = str(self.usernameTextField.text())
        email    = str(self.emailTextField.text())
        firstName= str(self.firstNameTextField.text())
        lastName = str(self.lastNameTextField.text())

        conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                               database=self.db.DB_NAME)
        mycursor = conn.cursor()
        query = "UPDATE managers SET username='%s',email='%s',firstname='%s',lastname='%s' WHERE id=%s" % (
        username,email,firstName,lastName,self.LOGGED_USER_ID)
        mycursor.execute(query)
        conn.commit()
        self.close()


class plotactiv(QDialog):
    def __init__(self):
        """Initializes an instance of the Ui_SignUp class.
        Usage:
        -----------
            ui = Ui_SignUp()
        Return:
        -----------
            None
        """
        super(plotactiv, self).__init__()
        self.ui = loadUi(os.path.join(os.path.dirname(__file__), "plot_activ.ui"), self)

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self)
        layout = QVBoxLayout()
        layout.addWidget(self.toolbar)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
   
        self.plot()

    def plot(self):
        """
        
        """
        data = [random.random() for i in range(10)]
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(data, 'o-')
        self.canvas.draw()