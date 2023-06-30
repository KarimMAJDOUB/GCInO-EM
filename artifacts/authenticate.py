# -*- coding: utf-8 -*-

###################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
###################################################################################
import os
import sys

import pymysql.connections as MySQLdb
from PyQt6.QtWidgets import *
from PyQt6.QtWidgets import QDialog
from PyQt6.uic import loadUi
from configparser import ConfigParser
from database import Database
from gcino import gcinocorps

class login(QDialog):
    def __init__(self):
        """Initializes an instance of the login class.
        Usage:
        -----------
            ui = login()
        Return:
        -----------
            None
        """
        super(login, self).__init__()
        self.ui = loadUi(os.path.join(os.path.dirname(__file__), "login.ui"), self)
        self.ui.pushButton.clicked.connect(self.access)
        self.ui.button.clicked.connect(self.signUp)
        self.ui.button_2.clicked.connect(self.forgetPassword)

        self.db = Database()

    def access(self):
        """This function handles the login functionality in the user interface
        and authenticates the user credentials by communicating with the authentication server.
        Usage:
        -----------
            ui = login()
            ui.access()
        Return:
        -----------
            None
        Raises:
        -----------
            AuthenticationError: If the login credentials are invalid.
            ConnectionError: If there is a problem connecting to the authentication server.
        """
        user=str(self.lineEdit.text())
        pwd=str(self.lineEdit_2.text())
        if len(user)==0 or len(pwd)==0:
            self.label_6.setText("Incorrect username or Password")
            self.label_6.setStyleSheet("color: red")
        else:
            try:
                conn = MySQLdb.Connection(host=self.db.DB_SERVER, user=self.db.DB_USERNAME, password=self.db.DB_PASSWORD,
                                       database=self.db.DB_NAME)
                cursor = conn.cursor()
                query = f"SELECT id, email, password, username FROM managers WHERE email='{user}' and password='{pwd}'"
                cursor.execute(query)
                data = cursor.fetchone()
                if len(data) > 0:
                    config_object = ConfigParser()
                    config_object.read("config.ini")
                    userinfo = config_object["USERINFO"]
                    userinfo["LOGGED_USER_ID"] = str(data[0])
                    with open('config.ini', 'w') as conf:
                        config_object.write(conf)

                    self.label_6.setText("successfull")
                    obj = gcinocorps()
                    widget.addWidget(obj)
                    widget.setCurrentIndex(widget.currentIndex() + 1)
                    widget.showMaximized()
                else:
                    self.label_6.setText("Incorrect username or Password")
                    self.label_6.setStyleSheet("color: red")
            except Exception as e:
                QMessageBox.about(self, "Error", "error : "+ str(e))

    def signUp(self):
        """This function handles the sign-up functionality in the user interface.
        Usage:
        -----------
            ui = Ui_login()
            ui.signup()
        Return:
        -----------
            None
        Raises:
        -----------
            RegistrationError: If there is an error during the registration process.
            ConnectionError: If there is a problem connecting to the registration server.
        """
        obj = signup()
        widget.addWidget(obj)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def forgetPassword(self):
        """ This function handles the forgot password functionality in the user interface
        Usage:
        -----------
            ui = Ui_login()
            ui.forget_Password()
        Returns:
        -----------
            None
        Raises:
        -----------
            ResetPasswordError: If there is an error during the password reset process.
            ConnectionError: If there is a problem connecting to the password reset server.
        """
        obj = forgetpassword()
        widget.addWidget(obj)
        widget.setCurrentIndex(widget.currentIndex()+1)

class signup(QDialog):
    def __init__(self):
        """Initializes an instance of the Ui_SignUp class.
        Usage:
        -----------
            ui = Ui_SignUp()
        Return:
        -----------
            None
        """
        super(signup, self).__init__()
        self.ui = loadUi(os.path.join(os.path.dirname(__file__), "signin.ui"), self)
        self.ui.pushButton.clicked.connect(self.register)
        self.ui.pushButton_2.clicked.connect(self.goback)

        self.db = Database()

    def goback(self):
        """This function allows the user to navigate back to the previous screen in the application.
        Usage:
        -----------
            ui = Ui_SignUp()
            ui.goback()
        Return:
        -----------
            None
        """
        obj=login()
        widget.addWidget(obj)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def register(self):
        """This function sends the user registration information to the registration server for account creation.
        Usage:
        -----------
            ui = signup()
            ui.register()
        Return:
        -----------
            *bool* : True if the registration is successful, False otherwise.
        Raises:
        -----------
            ConnectionError: If there is a problem connecting to the registration server.
        """
        firstname = self.lineEdit.text()
        lastname = self.lineEdit_2.text()
        mail = self.lineEdit_3.text()
        pwd = self.lineEdit_4.text()
        confirmpwd = self.lineEdit_5.text()
        username = self.lineEdit_6.text()
        if (len(firstname) and len(lastname) and len(pwd) and len(mail)
            and len(confirmpwd) and len(username)) == 0:
            self.error.setText("Please fill all Credentials")
            self.error.setStyleSheet("color:red")
        else:
            if pwd == confirmpwd:
                try:
                    conn = MySQLdb.connect(host=self.db.DB_SERVER, user=self.db.DB_USERNAME,
                                           password=self.db.DB_PASSWORD,
                                           database=self.db.DB_NAME)
                    cur = conn.cursor()
                    id_query="""SELECT
                                    max(id)
                                FROM
                                    managers
                             """
                    cur.execute(id_query)
                    R=cur.fetchone()
                    if R!=None and R[0]!=None:
                        id=int(R[0])+1
                    cur = conn.cursor()
                    sql_query="""INSERT INTO
                                    managers(id,firstname,lastname,username,email,Password)
                                 VALUES
                                    (%s, %s, %s, %s, %s, %s)
                              """
                    cur.execute(sql_query,(id,firstname,lastname,username,mail,pwd))
                    conn.commit()
                    if cur.fetchone():
                        self.error.setText("ERROR")
                    else:
                         self.error.setText("Sign Up Successfull ")
                         self.error.setStyleSheet("color:green")

                except Exception as e:
                    QMessageBox.about(self, "Error", "error : "+ str(e))
            else:
                self.error.setText("Passwords don't match")
                self.error.setStyleSheet("color:red")

class forgetpassword(QDialog):
    def __init__(self):
        """Initializes an instance of the Ui_ForgetPassword class.
        Usage:
        -----------
            ui = Ui_ForgetPassword()
        Return:
        -----------
            None
        """
        super(forgetpassword, self).__init__()
        self.ui = loadUi(os.path.join(os.path.dirname(__file__), "password.ui"), self)
        print(os.path.join(os.path.dirname(__file__), "password.ui"))
        self.ui.pushButton.clicked.connect(self.resetPassword)
        self.ui.pushButton_2.clicked.connect(self.goback)

    def goback(self):
        """This function allows the user to navigate back to the previous screen in the application.
        Usage:
        -----------
            ui = Ui_ForgetPassword()
            ui.goback()

        Return:
        -----------
            None
        """
        obj=login()
        widget.addWidget(obj)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def resetPassword(self):
        """ This function handles the forgot password functionality in the user interface
            and sends a password reset request to the password reset server
            for the given email address.
        Usage:
        -----------
            ui = Ui_ForgetPassword()
            ui.resetPassword()

        Returns:
        -----------
            None

        Raises:
        -----------
            ResetPasswordError: If there is an error during the password reset process.
            ConnectionError: If there is a problem connecting to the password reset server.
        """
        mail = self.lineEdit.text()
        new_pwd = self.lineEdit_2.text()
        conf_new_pwd = self.lineEdit_3.text()
        if (len(mail) and len(new_pwd) and len(conf_new_pwd)) == 0:
            self.error.setText("Please fill all Credentials")
            self.error.setStyleSheet("color:red")

        else:
            if new_pwd == conf_new_pwd:
                mydb = MySQLdb.Connection(host='localhost',
                                                database='fakegcino',
                                                user='root',
                                                password='Krayem99882056&&&'
                                                )
                sql_query = "select email from managers where email = %s"
                cur = mydb.cursor()
                cur.execute(sql_query,(mail,))
                result = cur.fetchall()
                if not result:
                    self.error.setText("This user does not exist, please sign up!")
                    self.error.setStyleSheet("color:red")
                elif (mail == result[0][0]):
                        mydb = MySQLdb.Connection(host='localhost',
                                                database='fakegcino',
                                                user='root',
                                                password='Krayem99882056&&&'
                                                )
                        sql_query = "UPDATE managers SET password = %s WHERE email = %s"
                        cur = mydb.cursor()
                        cur.execute(sql_query,(new_pwd,mail))
                        mydb.commit()
                        if cur.fetchone():
                            self.error.setText("ERROR")
                        else:
                            self.error.setText("Done!")
                            self.error.setStyleSheet("color:green")
            else:
                self.error.setText("Passwords don't match")
if __name__ =="__main__":
    app = QApplication([])
    welcome= login()
    widget = QStackedWidget()
    width = widget.frameGeometry().width()
    height = widget.frameGeometry().height()
    
    widget.addWidget(welcome)
    widget.showMaximized()
    try:
        sys.exit((app.exec()))
    except:
        print("Exiting")