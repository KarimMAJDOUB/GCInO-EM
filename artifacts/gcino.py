# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
import sys
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QApplication, QDialog
from PyQt6.uic import loadUi
from setup import gcinodesign, gcinotree, gcinotables, gcinobox
from events import eventshandler, filterevents
from forms import modifyform

class gcinocorps(QMainWindow):
    def __init__(self):
        super(gcinocorps, self).__init__()
        self.ui = loadUi(os.path.join(os.path.dirname(__file__), "corps.ui"), self)
        self.query_list =[f"SELECT DISTINCT projectname FROM projects", f"SELECT DISTINCT CONCAT(firstName , ' ' , lastname) FROM managers",
                          f"SELECT operation_datetime FROM object_dist", f"SELECT Distinct actions FROM object_dist", f"SELECT DISTINCT Type_object FROM object_dist"
                        ]
        self.Box_list = [self.ui.Why_Box, self.ui.Who_Box, self.ui.date_Box, self.ui.action_box, self.ui.What_Box]
        self.col_list = ["project_name", "name", "operation_datetime", "actions", "Type_object" ]
        
        self.gcino_window = gcinodesign(self.ui.tableWidget, self.ui.tableWidget_2, self.ui.tab_3)
        self.gcino_tree = gcinotree(self.ui.treeWidget, self.ui.treeWidget_2)
        self.gcino_table = gcinotables(self.ui.tableWidget, self.ui.tableWidget_2, self.ui.export_csv_btn, self.ui.What_Box)
        for i in range(len(self.query_list)-1):
            self.Box = gcinobox(self.Box_list[i], self.query_list[i], type="all")
        self.Box = gcinobox(self.Box_list[len(self.query_list)-1], self.query_list[len(self.query_list)-1], type="one")
        
        self.filter = filterevents(self.Box_list,self.ui.tableWidget_2,self.ui.tableWidget,self.col_list, self.ui.treeWidget,self.ui.treeWidget_2, self.ui.search, type='all')
        
        self.returnForms()
          
    def returnForms(self):
        self.ui.insertDataButton.clicked.connect(eventshandler.openInsertionForm)
        self.ui.profileButton.clicked.connect(eventshandler.openProfileForm)
        self.ui.projectButton.clicked.connect(eventshandler.openProjForm)
        self.ui.btn_plot_act.clicked.connect(eventshandler.openPlotForm)
        self.ui.tableWidget.cellClicked.connect(modifyform(self.ui.tableWidget).exec)
        self.ui.treeWidget.clicked.connect(self.filter.filterTree)
        self.ui.treeWidget_2.clicked.connect(self.filter.filterLocationTree)
        
        for combo_box in self.Box_list:
            combo_box.currentIndexChanged.connect(self.filter.filterBox)
        self.ui.reset_btn.clicked.connect(self.filter.resetTable)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = gcinocorps()
    window.show()
    sys.exit(app.exec())