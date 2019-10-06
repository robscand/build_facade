# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mkplan.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(335, 151)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.inpCode = QtWidgets.QLineEdit(Dialog)
        self.inpCode.setObjectName("inpCode")
        self.verticalLayout.addWidget(self.inpCode)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.inpYear = QtWidgets.QDateEdit(Dialog)
        self.inpYear.setObjectName("inpYear")
        self.verticalLayout_2.addWidget(self.inpYear)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(Dialog)
        self.radioButton.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 2, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.inpName = QtWidgets.QLineEdit(Dialog)
        self.inpName.setText("")
        self.inpName.setObjectName("inpName")
        self.gridLayout.addWidget(self.inpName, 1, 1, 1, 1)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Выбор объекта"))
        self.label_2.setText(_translate("Dialog", "Код типа объекта:"))
        self.inpCode.setToolTip(_translate("Dialog", "Допускается ввод только целых чисел"))
        self.inpCode.setPlaceholderText(_translate("Dialog", "Введите число"))
        self.label_5.setText(_translate("Dialog", "Год:"))
        self.inpYear.setDisplayFormat(_translate("Dialog", "yyyy"))
        self.radioButton.setText(_translate("Dialog", "Корректировать сроки выполнения работ"))
        self.label_4.setText(_translate("Dialog", "Наименование\n"
"объекта:"))
        self.inpName.setToolTip(_translate("Dialog", "Введите предложение на русском.\n"
"В качестве разделителя допустимы только пробелы."))
        self.inpName.setPlaceholderText(_translate("Dialog", "Введите текст"))
        self.label.setText(_translate("Dialog", "\n"
"Код объекта:"))

