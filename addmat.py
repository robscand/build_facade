# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addmat.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(292, 131)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.inpUn = QtWidgets.QLineEdit(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inpUn.sizePolicy().hasHeightForWidth())
        self.inpUn.setSizePolicy(sizePolicy)
        self.inpUn.setMaximumSize(QtCore.QSize(100, 16777215))
        self.inpUn.setObjectName("inpUn")
        self.horizontalLayout.addWidget(self.inpUn)
        self.comboUn = QtWidgets.QComboBox(Dialog)
        self.comboUn.setObjectName("comboUn")
        self.horizontalLayout.addWidget(self.comboUn)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.inpCode = QtWidgets.QLineEdit(Dialog)
        self.inpCode.setObjectName("inpCode")
        self.gridLayout.addWidget(self.inpCode, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.inpName = QtWidgets.QLineEdit(Dialog)
        self.inpName.setObjectName("inpName")
        self.gridLayout.addWidget(self.inpName, 1, 1, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Ввод данных материала"))
        self.inpUn.setPlaceholderText(_translate("Dialog", "Введите число"))
        self.label_3.setText(_translate("Dialog", "Единица\n"
"измерения:"))
        self.label_2.setText(_translate("Dialog", "Наименование\n"
"материала:"))
        self.label.setText(_translate("Dialog", "Шифр материала:"))
        self.inpName.setPlaceholderText(_translate("Dialog", "Введите текст"))

