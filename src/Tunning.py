# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tunning.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tunning_parameters(object):
    def setupUi(self, Tunning_parameters):
        Tunning_parameters.setObjectName("Tunning_parameters")
        Tunning_parameters.resize(306, 318)
        self.centralwidget = QtWidgets.QWidget(Tunning_parameters)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 30, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 80, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 130, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 180, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.Kp = QtWidgets.QLineEdit(self.centralwidget)
        self.Kp.setGeometry(QtCore.QRect(100, 90, 113, 21))
        self.Kp.setObjectName("Kp")
        self.KI = QtWidgets.QLineEdit(self.centralwidget)
        self.KI.setGeometry(QtCore.QRect(100, 140, 113, 21))
        self.KI.setObjectName("KI")
        self.KD = QtWidgets.QLineEdit(self.centralwidget)
        self.KD.setGeometry(QtCore.QRect(100, 190, 113, 21))
        self.KD.setObjectName("KD")
        self.Apply_par = QtWidgets.QPushButton(self.centralwidget)
        self.Apply_par.setGeometry(QtCore.QRect(80, 230, 121, 41))
        self.Apply_par.setObjectName("Apply_par")
        Tunning_parameters.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Tunning_parameters)
        self.statusbar.setObjectName("statusbar")
        Tunning_parameters.setStatusBar(self.statusbar)

        self.retranslateUi(Tunning_parameters)
        QtCore.QMetaObject.connectSlotsByName(Tunning_parameters)

    def retranslateUi(self, Tunning_parameters):
        _translate = QtCore.QCoreApplication.translate
        Tunning_parameters.setWindowTitle(_translate("Tunning_parameters", "Tunning"))
        self.label.setText(_translate("Tunning_parameters", "Closed Loop Parameters"))
        self.label_2.setText(_translate("Tunning_parameters", "Kp"))
        self.label_3.setText(_translate("Tunning_parameters", "KI"))
        self.label_4.setText(_translate("Tunning_parameters", "KD"))
        self.Apply_par.setText(_translate("Tunning_parameters", "Apply"))