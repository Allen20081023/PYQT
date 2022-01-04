# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stats.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_form(object):
    def setupUi(self, form):
        form.setObjectName("form")
        form.resize(532, 600)
        self.Form = QtWidgets.QWidget(form)
        self.Form.setObjectName("Form")
        self.TextEdit = QtWidgets.QPlainTextEdit(self.Form)
        self.TextEdit.setGeometry(QtCore.QRect(10, 10, 511, 471))
        self.TextEdit.setObjectName("TextEdit")
        self.button = QtWidgets.QPushButton(self.Form)
        self.button.setGeometry(QtCore.QRect(230, 490, 75, 23))
        self.button.setObjectName("button")
        form.setCentralWidget(self.Form)
        self.menubar = QtWidgets.QMenuBar(form)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 532, 23))
        self.menubar.setObjectName("menubar")
        form.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(form)
        self.statusbar.setObjectName("statusbar")
        form.setStatusBar(self.statusbar)

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "统计薪资"))
        self.TextEdit.setPlaceholderText(_translate("form", "请输入薪资信息"))
        self.button.setText(_translate("form", "统计"))

