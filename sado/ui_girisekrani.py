# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/boran/Desktop/Bütün VSCODE dosyalarım/sado/girisekrani.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(908, 806)
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 721, 491))
        self.widget.setStyleSheet("background-color: rgb(149, 149, 149);")
        self.widget.setObjectName("widget")
        self.google = QtWidgets.QPushButton(self.widget)
        self.google.setGeometry(QtCore.QRect(30, 200, 191, 41))
        self.google.setStyleSheet("QPushButton {\n"
"            background-color: rgb(0, 0, 0);\n"
"color: rgb(228, 228, 228);\n"
"border-color: black;\n"
"border-radius: 15px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"font: 10pt \"Luminari\";\n"
"        }\n"
"        QPushButton:hover {\n"
"           border-color:#0F9D58;\n"
"           color: #0F9D58; \n"
"           \n"
"            background-color: black;\n"
"           border-width: 2px;\n"
"        }")
        self.google.setObjectName("google")
        self.twitter = QtWidgets.QPushButton(self.widget)
        self.twitter.setGeometry(QtCore.QRect(30, 310, 191, 41))
        self.twitter.setStyleSheet("QPushButton {\n"
"            background-color: rgb(0, 0, 0);\n"
"color: rgb(228, 228, 228);\n"
"border-color: black;\n"
"border-radius: 15px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"font: 10pt \"Luminari\";\n"
"        }\n"
"        QPushButton:hover {\n"
"           border-color: #1DA1F2;\n"
"           color: #1DA1F2; \n"
"           \n"
"            background-color: black;\n"
"           border-width: 2px;\n"
"        }")
        self.twitter.setObjectName("twitter")
        self.title = QtWidgets.QLabel(self.widget)
        self.title.setGeometry(QtCore.QRect(260, 0, 221, 91))
        self.title.setStyleSheet("font: 38pt \"Luminari\";\n"
"color: rgb(218, 218, 218);")
        self.title.setText("")
        self.title.setPixmap(QtGui.QPixmap("saboo.png"))
        self.title.setObjectName("title")
        self.reddit = QtWidgets.QPushButton(self.widget)
        self.reddit.setGeometry(QtCore.QRect(500, 310, 191, 41))
        self.reddit.setStyleSheet("QPushButton {\n"
"            background-color: rgb(0, 0, 0);\n"
"color: rgb(228, 228, 228);\n"
"border-color: black;\n"
"border-radius: 15px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"font: 10pt \"Luminari\";\n"
"        }\n"
"        QPushButton:hover {\n"
"           border-color: #FF5700;\n"
"           color: #FF5700; \n"
"           \n"
"            background-color: black;\n"
"           border-width: 2px;\n"
"        }")
        self.reddit.setObjectName("reddit")
        self.youtube = QtWidgets.QPushButton(self.widget)
        self.youtube.setGeometry(QtCore.QRect(500, 200, 191, 41))
        self.youtube.setStyleSheet("QPushButton {\n"
"            background-color: rgb(0, 0, 0);\n"
"color: rgb(228, 228, 228);\n"
"border-color: black;\n"
"border-radius: 15px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"font: 10pt \"Luminari\";\n"
"        }\n"
"        QPushButton:hover {\n"
"           border-color: #FF0000;\n"
"           color: #FF0000; \n"
"           \n"
"            background-color: black;\n"
"           border-width: 2px;\n"
"        }")
        self.youtube.setObjectName("youtube")
        self.instagram = QtWidgets.QPushButton(self.widget)
        self.instagram.setGeometry(QtCore.QRect(270, 310, 191, 41))
        self.instagram.setStyleSheet("QPushButton {\n"
"            background-color: rgb(0, 0, 0);\n"
"color: rgb(228, 228, 228);\n"
"border-color: black;\n"
"border-radius: 15px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"font: 10pt \"Luminari\";\n"
"        }\n"
"        QPushButton:hover {\n"
"           border-color: #C13584;\n"
"           color: #C13584; \n"
"           \n"
"            background-color: black;\n"
"           border-width: 2px;\n"
"        }")
        self.instagram.setObjectName("instagram")
        self.facebook = QtWidgets.QPushButton(self.widget)
        self.facebook.setGeometry(QtCore.QRect(270, 200, 191, 41))
        self.facebook.setStyleSheet("QPushButton {\n"
"            background-color: rgb(0, 0, 0);\n"
"color: rgb(228, 228, 228);\n"
"border-color: black;\n"
"border-radius: 15px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"font: 10pt \"Luminari\";\n"
"        }\n"
"        QPushButton:hover {\n"
"           border-color:#4267B2;\n"
"           color: #4267B2; \n"
"           \n"
"            background-color: black;\n"
"           border-width: 2px;\n"
"        }")
        self.facebook.setObjectName("facebook")
        self.twitch = QtWidgets.QPushButton(self.widget)
        self.twitch.setGeometry(QtCore.QRect(500, 420, 191, 41))
        self.twitch.setStyleSheet("QPushButton {\n"
"            background-color: rgb(0, 0, 0);\n"
"color: rgb(228, 228, 228);\n"
"border-color: black;\n"
"border-radius: 15px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"font: 10pt \"Luminari\";\n"
"        }\n"
"        QPushButton:hover {\n"
"           border-color: #6441a5;\n"
"           color: #6441a5; \n"
"           \n"
"            background-color: black;\n"
"           border-width: 2px;\n"
"        }")
        self.twitch.setObjectName("twitch")
        self.netflix = QtWidgets.QPushButton(self.widget)
        self.netflix.setGeometry(QtCore.QRect(270, 420, 191, 41))
        self.netflix.setStyleSheet("QPushButton {\n"
"            background-color: rgb(0, 0, 0);\n"
"color: rgb(228, 228, 228);\n"
"border-color: black;\n"
"border-radius: 15px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"font: 10pt \"Luminari\";\n"
"        }\n"
"        QPushButton:hover {\n"
"           border-color: #E50914;\n"
"           color: #E50914; \n"
"           \n"
"            background-color: black;\n"
"           border-width: 2px;\n"
"        }")
        self.netflix.setObjectName("netflix")
        self.amazon = QtWidgets.QPushButton(self.widget)
        self.amazon.setGeometry(QtCore.QRect(30, 420, 191, 41))
        self.amazon.setStyleSheet("QPushButton {\n"
"            background-color: black;\n"
"color: rgb(228, 228, 228);\n"
"border-color: black;\n"
"border-radius: 15px;\n"
"border-style: solid;\n"
"border-width: 2px;\n"
"font: 10pt \"Luminari\";\n"
"        }\n"
"        QPushButton:hover {\n"
"           border-color: #FF9900;\n"
"           color: white; \n"
"           \n"
"            background-color: black;\n"
"           border-width: 2px;\n"
"        }")
        self.amazon.setObjectName("amazon")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 110, 651, 41))
        self.label.setStyleSheet("font: 25pt \"Luminari\";\n"
"color: white;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(100, 270, 41, 31))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("twitter.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(100, 160, 41, 31))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("google.png"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(350, 160, 41, 31))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("facebook.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(580, 160, 41, 31))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("youtube.png"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(350, 270, 41, 31))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("instagram.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(350, 380, 41, 31))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("netflix.png"))
        self.label_8.setScaledContents(True)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.widget)
        self.label_9.setGeometry(QtCore.QRect(100, 380, 41, 31))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("amazon.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(580, 270, 41, 31))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("reddit.png"))
        self.label_10.setScaledContents(True)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(580, 380, 41, 31))
        self.label_11.setText("")
        self.label_11.setPixmap(QtGui.QPixmap("twitch.png"))
        self.label_11.setScaledContents(True)
        self.label_11.setObjectName("label_11")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.google.setText(_translate("Dialog", "Google"))
        self.twitter.setText(_translate("Dialog", "Twitter"))
        self.reddit.setText(_translate("Dialog", "Reddit"))
        self.youtube.setText(_translate("Dialog", "Youtube"))
        self.instagram.setText(_translate("Dialog", "Instagram"))
        self.facebook.setText(_translate("Dialog", "Facebook"))
        self.twitch.setText(_translate("Dialog", "Twitch"))
        self.netflix.setText(_translate("Dialog", "Netflix"))
        self.amazon.setText(_translate("Dialog", "Amazon"))
        self.label.setText(_translate("Dialog", "Please select the website you want to go to"))

