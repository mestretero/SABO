# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/boran/Desktop/Bütün VSCODE dosyalarım/sado/netflix.ui'
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
        self.webEngineView.setUrl(QtCore.QUrl("https://www.netflix.com/tr-en/login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse"))
        self.webEngineView.setZoomFactor(0.75)
        self.webEngineView.setObjectName("webEngineView")
        self.back = QtWidgets.QPushButton(self.widget)
        self.back.setGeometry(QtCore.QRect(0, 460, 51, 20))
        self.back.setStyleSheet("background-color: gray;\n"
"color:black;\n"
"\n"
"border-radius: 10px")
        self.back.setObjectName("back")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.back.setText(_translate("Dialog", "back"))

from PyQt5 import QtWebEngineWidgets
