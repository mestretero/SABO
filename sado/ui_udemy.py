# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/boran/Desktop/Bütün VSCODE dosyalarım/sado/udemy.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(720, 480)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 721, 491))
        self.widget.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.widget.setObjectName("widget")
        self.webEngineView = QtWebEngineWidgets.QWebEngineView(self.widget)
        self.webEngineView.setGeometry(QtCore.QRect(-1, -1, 721, 491))
        self.webEngineView.setUrl(QtCore.QUrl("https://www.udemy.com/"))
        self.webEngineView.setZoomFactor(0.75)
        self.webEngineView.setObjectName("webEngineView")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

from PyQt5 import QtWebEngineWidgets
