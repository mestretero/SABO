# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\BÜTÜN VSCODE DOSYALARI\sado\yeniekran.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(720, 480)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 721, 491))
        self.widget.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.widget.setObjectName("widget")
        self.username = QtWidgets.QLineEdit(self.widget)
        self.username.setGeometry(QtCore.QRect(290, 160, 131, 41))
        self.username.setAutoFillBackground(False)
        self.username.setStyleSheet("QLineEdit {\n"
"            background-color: rgb(0, 0, 0);\n"
"color: rgb(228, 228, 228);\n"
"border-color: black;\n"
"border-radius: 15px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"font: 10pt \"Luminari\";\n"
"        }\n"
"        QLineEdit:focus {\n"
"           border-color: yellow;\n"
"        }")
        self.username.setFrame(True)
        self.username.setCursorPosition(0)
        self.username.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.username.setDragEnabled(False)
        self.username.setReadOnly(False)
        self.username.setObjectName("username")
        self.password = QtWidgets.QLineEdit(self.widget)
        self.password.setGeometry(QtCore.QRect(290, 220, 131, 41))
        self.password.setStyleSheet("QLineEdit {\n"
"            background-color: rgb(0, 0, 0);\n"
"color: rgb(228, 228, 228);\n"
"border-color: black;\n"
"border-radius: 15px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"font: 10pt \"Luminari\";\n"
"        }\n"
"        QLineEdit:focus {\n"
"           border-color: yellow;\n"
"        }")
        self.password.setClearButtonEnabled(False)
        self.password.setObjectName("password")
        self.login = QtWidgets.QPushButton(self.widget)
        self.login.setGeometry(QtCore.QRect(260, 340, 191, 41))
        self.login.setStyleSheet("QPushButton {\n"
"            background-color: rgb(0, 0, 0);\n"
"color: rgb(228, 228, 228);\n"
"border-color: black;\n"
"border-radius: 15px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"font: 10pt \"Luminari\";\n"
"        }\n"
"        QPushButton:hover {\n"
"           border-color: yellow;\n"
"           color: yellow; \n"
"           \n"
"            background-color: black;\n"
"           border-width: 2px;\n"
"        }")
        self.login.setObjectName("login")
        self.register_2 = QtWidgets.QPushButton(self.widget)
        self.register_2.setGeometry(QtCore.QRect(260, 390, 191, 41))
        self.register_2.setStyleSheet("QPushButton {\n"
"            background-color: rgb(0, 0, 0);\n"
"color: rgb(228, 228, 228);\n"
"border-color: black;\n"
"border-radius: 15px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"font: 10pt \"Luminari\";\n"
"        }\n"
"        QPushButton:hover {\n"
"           border-color: yellow;\n"
"           color: yellow; \n"
"           \n"
"            background-color: black;\n"
"           border-width: 2px;\n"
"        }")
        self.register_2.setObjectName("register_2")
        self.title = QtWidgets.QLabel(self.widget)
        self.title.setGeometry(QtCore.QRect(250, 60, 221, 81))
        self.title.setStyleSheet("font: 38pt \"Luminari\";\n"
"color: white;")
        self.title.setText("")
        self.title.setPixmap(QtGui.QPixmap("d:\\BÜTÜN VSCODE DOSYALARI\\sado\\saboo.png"))
        self.title.setScaledContents(False)
        self.title.setObjectName("title")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(200, 460, 331, 16))
        self.label_2.setObjectName("label_2")
        self.error = QtWidgets.QLabel(self.widget)
        self.error.setGeometry(QtCore.QRect(290, 280, 141, 41))
        self.error.setStyleSheet("font: 10pt \"Luminari\";\n"
"color: rgb(124, 0, 0);")
        self.error.setText("")
        self.error.setObjectName("error")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.username.setPlaceholderText(_translate("Dialog", "    Username"))
        self.password.setPlaceholderText(_translate("Dialog", "    Password"))
        self.login.setText(_translate("Dialog", "Login"))
        self.register_2.setText(_translate("Dialog", "Register"))
        self.label_2.setText(_translate("Dialog", "Saadet Allahyarova Tarafından Tasarlanmıştır Tüm Hakları Saklıdır ™"))