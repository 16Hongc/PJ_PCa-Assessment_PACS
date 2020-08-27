# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(936, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.image_save = QtWidgets.QPushButton(self.centralwidget)
        self.image_save.setGeometry(QtCore.QRect(720, 529, 101, 41))
        self.image_save.setObjectName("image_save")
        self.image_cancer_predict = QtWidgets.QPushButton(self.centralwidget)
        self.image_cancer_predict.setGeometry(QtCore.QRect(500, 529, 101, 41))
        self.image_cancer_predict.setObjectName("image_cancer_predict")
        self.image_search_cancer = QtWidgets.QPushButton(self.centralwidget)
        self.image_search_cancer.setGeometry(QtCore.QRect(610, 529, 101, 41))
        self.image_search_cancer.setObjectName("image_search_cancer")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(320, 529, 171, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        self.re_patient_list = QtWidgets.QPushButton(self.centralwidget)
        self.re_patient_list.setGeometry(QtCore.QRect(240, 370, 71, 31))
        self.re_patient_list.setObjectName("re_patient_list")
        self.search_patient = QtWidgets.QPushButton(self.centralwidget)
        self.search_patient.setGeometry(QtCore.QRect(160, 370, 71, 31))
        self.search_patient.setObjectName("search_patient")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 370, 131, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.patient_list = QtWidgets.QTreeView(self.centralwidget)
        self.patient_list.setGeometry(QtCore.QRect(20, 200, 291, 161))
        self.patient_list.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.patient_list.setObjectName("patient_list")
        self.treeView = QtWidgets.QTreeView(self.centralwidget)
        self.treeView.setGeometry(QtCore.QRect(20, 411, 291, 161))
        self.treeView.setObjectName("treeView")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 7, 291, 183))
        self.calendarWidget.setObjectName("calendarWidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(320, 10, 501, 511))
        self.graphicsView.setDragMode(QtWidgets.QGraphicsView.RubberBandDrag)
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(830, 10, 31, 31))
        self.pushButton.setObjectName("pushButton")
        self.minusbutton = QtWidgets.QPushButton(self.centralwidget)
        self.minusbutton.setGeometry(QtCore.QRect(830, 50, 31, 31))
        self.minusbutton.setObjectName("minusbutton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.image_save.setText(_translate("MainWindow", "Save"))
        self.image_cancer_predict.setText(_translate("MainWindow", "Prediction"))
        self.image_search_cancer.setText(_translate("MainWindow", "Search"))
        self.re_patient_list.setText(_translate("MainWindow", "새로고침"))
        self.search_patient.setText(_translate("MainWindow", "검 색"))
        self.pushButton.setText(_translate("MainWindow", "+"))
        self.minusbutton.setText(_translate("MainWindow", "-"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())