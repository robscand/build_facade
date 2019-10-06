# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addwmat.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(319, 131)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comWork = QtWidgets.QComboBox(Dialog)
        self.comWork.setObjectName("comWork")
        self.gridLayout.addWidget(self.comWork, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comMat = QtWidgets.QComboBox(Dialog)
        self.comMat.setObjectName("comMat")
        self.gridLayout.addWidget(self.comMat, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.inpVal = QtWidgets.QLineEdit(Dialog)
        self.inpVal.setObjectName("inpVal")
        self.gridLayout.addWidget(self.inpVal, 2, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Назначение материала"))
        self.label.setText(_translate("Dialog", "Обоснование:"))
        self.label_2.setText(_translate("Dialog", "Наименование\n"
"материала:"))
        self.label_3.setText(_translate("Dialog", "Норма расхода\n"
"на единицу объема:"))
        self.inpVal.setPlaceholderText(_translate("Dialog", "Введите число"))

