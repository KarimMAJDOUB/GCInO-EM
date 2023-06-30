# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
from PyQt6.QtWidgets import QMainWindow
from PyQt6.uic import loadUi
from setup import gcinodesign, gcinotree, gcinotables, gcinobox
from events import eventshandler, filterevents

class gcinocorps(QMainWindow):
    def __init__(self):
        super(gcinocorps, self).__init__()
        self.ui = loadUi(os.path.join(os.path.dirname(__file__), "corps.ui"), self)# Load the UI file
        self.query_list =[f"SELECT DISTINCT projectname FROM projects", f"SELECT DISTINCT CONCAT(firstName , ' ' , lastname) FROM managers", f"SELECT DISTINCT Type_object FROM object_dist",
                          f"SELECT operation_datetime FROM object_dist",   f"SELECT Distinct Quantity FROM object_dist", f"SELECT Distinct actions FROM object_dist"
                        ]
        self.Box_list = [self.ui.Why_Box, self.ui.Who_Box, self.ui.What_Box, self.ui.date_Box, self.ui.Quantity_Box, self.ui.action_box]
        self.col_list = ["project_name", "name", "Type_Object", "operation_datetime", "Quantity", "actions" ]
        
        self.gcino_window = gcinodesign(self.ui.tableWidget, self.ui.tableWidget_2)

        self.gcino_tree = gcinotree(self.ui.treeWidget)

        self.gcino_table = gcinotables(self.ui.tableWidget, self.ui.tableWidget_2)

        for i in range(len(self.query_list)):
            self.Box = gcinobox(self.Box_list[i], self.query_list[i])

        self.filter = filterevents(self.Box_list,self.ui.tableWidget_2,self.ui.tableWidget,self.col_list, self.ui.treeWidget)

        self.returnForms()
        
    def returnForms(self):
        self.ui.insertDataButton.clicked.connect(eventshandler.openInsertionForm)
        self.ui.profileButton.clicked.connect(eventshandler.openProfileForm)
        self.ui.btn_plot_act.clicked.connect(eventshandler.openPlotForm)
        self.ui.treeWidget.clicked.connect(self.filter.filterTree)
        for combo_box in self.Box_list:
            combo_box.currentIndexChanged.connect(self.filter.filterBox)
        self.ui.reset_btn.clicked.connect(self.filter.resetTable)
        


