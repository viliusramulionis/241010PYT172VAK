# Form implementation generated from reading ui file 'dizainas.ui'
#
# Created by: PyQt6 UI code generator 6.8.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.prideti = QtWidgets.QPushButton(parent=self.centralwidget)
        self.prideti.setGeometry(QtCore.QRect(500, 240, 111, 81))
        self.prideti.setObjectName("prideti")
        self.atimti = QtWidgets.QPushButton(parent=self.centralwidget)
        self.atimti.setGeometry(QtCore.QRect(210, 240, 111, 81))
        self.atimti.setObjectName("atimti")
        self.skaicius = QtWidgets.QLabel(parent=self.centralwidget)
        self.skaicius.setGeometry(QtCore.QRect(390, 250, 71, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.skaicius.setFont(font)
        self.skaicius.setObjectName("skaicius")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.prideti.setText(_translate("MainWindow", "PLIUS"))
        self.atimti.setText(_translate("MainWindow", "MINUS"))
        self.skaicius.setText(_translate("MainWindow", "15"))
