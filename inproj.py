# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'inproj.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(361, 413)
        self.gridLayout = QtWidgets.QGridLayout(dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.label_11 = QtWidgets.QLabel(dialog)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 7, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(dialog)
        self.label_9.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 5, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(dialog)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.inpName = QtWidgets.QLineEdit(dialog)
        self.inpName.setText("")
        self.inpName.setMaxLength(255)
        self.inpName.setObjectName("inpName")
        self.gridLayout.addWidget(self.inpName, 1, 1, 1, 3)
        self.inpReqCap = QtWidgets.QLineEdit(dialog)
        self.inpReqCap.setObjectName("inpReqCap")
        self.gridLayout.addWidget(self.inpReqCap, 6, 1, 1, 3)
        self.label_8 = QtWidgets.QLabel(dialog)
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.inpFinDate = QtWidgets.QDateEdit(dialog)
        self.inpFinDate.setAccelerated(False)
        self.inpFinDate.setCurrentSectionIndex(0)
        self.inpFinDate.setObjectName("inpFinDate")
        self.gridLayout.addWidget(self.inpFinDate, 7, 1, 1, 1)
        self.inpExpectCost = QtWidgets.QLineEdit(dialog)
        self.inpExpectCost.setObjectName("inpExpectCost")
        self.gridLayout.addWidget(self.inpExpectCost, 5, 1, 1, 3)
        self.inpAllVal = QtWidgets.QLineEdit(dialog)
        self.inpAllVal.setObjectName("inpAllVal")
        self.gridLayout.addWidget(self.inpAllVal, 8, 1, 1, 3)
        self.label_6 = QtWidgets.QLabel(dialog)
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(dialog)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.inpFullCost = QtWidgets.QLineEdit(dialog)
        self.inpFullCost.setObjectName("inpFullCost")
        self.gridLayout.addWidget(self.inpFullCost, 3, 1, 1, 3)
        self.inpStartDate = QtWidgets.QDateEdit(dialog)
        self.inpStartDate.setObjectName("inpStartDate")
        self.gridLayout.addWidget(self.inpStartDate, 4, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(dialog)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 6, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(dialog)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 8, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(dialog)
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.inpCode = QtWidgets.QLineEdit(dialog)
        self.inpCode.setObjectName("inpCode")
        self.verticalLayout.addWidget(self.inpCode)
        self.gridLayout.addLayout(self.verticalLayout, 0, 1, 1, 1)
        self.statusBox = QtWidgets.QComboBox(dialog)
        self.statusBox.setObjectName("statusBox")
        self.gridLayout.addWidget(self.statusBox, 2, 1, 1, 2)
        self.inpOwnVal = QtWidgets.QLineEdit(dialog)
        self.inpOwnVal.setObjectName("inpOwnVal")
        self.gridLayout.addWidget(self.inpOwnVal, 9, 1, 1, 3)
        self.label_15 = QtWidgets.QLabel(dialog)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 9, 0, 1, 1)
        self.radioButton = QtWidgets.QRadioButton(dialog)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 7, 2, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(dialog)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.inpYear = QtWidgets.QDateEdit(dialog)
        self.inpYear.setObjectName("inpYear")
        self.verticalLayout_2.addWidget(self.inpYear)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 2, 1, 1)
        self.label_16 = QtWidgets.QLabel(dialog)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 10, 0, 1, 1)
        self.inpExternVal = QtWidgets.QLineEdit(dialog)
        self.inpExternVal.setObjectName("inpExternVal")
        self.gridLayout.addWidget(self.inpExternVal, 10, 1, 1, 3)

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "Ввод данных об объекте"))
        self.label_11.setText(_translate("dialog", "Срок ввода\n"
"в эксплуатацию:"))
        self.label_9.setText(_translate("dialog", "Ожидаемое\n"
"выполнение работ\n"
" к началу года, млн. руб.:"))
        self.label_4.setText(_translate("dialog", "Наименование объекта:"))
        self.inpName.setToolTip(_translate("dialog", "Введите предложение на русском.\n"
"В качестве разделителя допустимы только пробелы."))
        self.inpName.setPlaceholderText(_translate("dialog", "Введите текст"))
        self.inpReqCap.setToolTip(_translate("dialog", "Допускается ввод только целых чисел"))
        self.inpReqCap.setPlaceholderText(_translate("dialog", "Введите число"))
        self.label_8.setText(_translate("dialog", "Срок начала\n"
"строительства:"))
        self.inpFinDate.setDisplayFormat(_translate("dialog", "dd.MM.yy"))
        self.inpExpectCost.setToolTip(_translate("dialog", "Допускается ввод только целых чисел."))
        self.inpExpectCost.setPlaceholderText(_translate("dialog", "Введите число"))
        self.inpAllVal.setToolTip(_translate("dialog", "Допускается ввод только целых чисел."))
        self.inpAllVal.setPlaceholderText(_translate("dialog", "Введите число"))
        self.label_6.setText(_translate("dialog", "Статус объекта:"))
        self.label.setText(_translate("dialog", "\n"
"Код объекта:"))
        self.inpFullCost.setToolTip(_translate("dialog", "Допускается ввод только целых чисел."))
        self.inpFullCost.setPlaceholderText(_translate("dialog", "Введите число"))
        self.inpStartDate.setDisplayFormat(_translate("dialog", "dd.MM.yy"))
        self.label_10.setText(_translate("dialog", "Вводимая мощность\n"
"в текущем году, м2:"))
        self.label_12.setText(_translate("dialog", "Весь объем работ\n"
"на текущий год, млн. руб:"))
        self.label_7.setText(_translate("dialog", "Полная сметная\n"
"стоимость, млн. руб.:"))
        self.label_2.setText(_translate("dialog", "Код типа объекта:"))
        self.inpCode.setToolTip(_translate("dialog", "Допускается ввод только целых чисел"))
        self.inpCode.setPlaceholderText(_translate("dialog", "Введите число"))
        self.inpOwnVal.setToolTip(_translate("dialog", "Допускается ввод только целых чисел."))
        self.inpOwnVal.setPlaceholderText(_translate("dialog", "Введите число"))
        self.label_15.setText(_translate("dialog", "Объем работ\n"
"организации, млн. руб:"))
        self.radioButton.setText(_translate("dialog", "Неизвестно"))
        self.label_5.setText(_translate("dialog", "Год:"))
        self.inpYear.setDisplayFormat(_translate("dialog", "yyyy"))
        self.label_16.setText(_translate("dialog", "Объем работ\n"
"субподряда, млн. руб.:"))
        self.inpExternVal.setToolTip(_translate("dialog", "Допускается ввод только целых чисел."))
        self.inpExternVal.setPlaceholderText(_translate("dialog", "Введите число"))
