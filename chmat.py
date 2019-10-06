# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chmat.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(236, 87)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.rButt_new = QtWidgets.QRadioButton(Dialog)
        self.rButt_new.setObjectName("rButt_new")
        self.verticalLayout.addWidget(self.rButt_new)
        self.rButt_old = QtWidgets.QRadioButton(Dialog)
        self.rButt_old.setObjectName("rButt_old")
        self.verticalLayout.addWidget(self.rButt_old)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Добавить материал"))
        self.rButt_new.setText(_translate("Dialog", "Добавить новый материал"))
        self.rButt_old.setText(_translate("Dialog", "Назначить материал на работу"))

