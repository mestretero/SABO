import sqlite3
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QStackedWidget, QInputDialog, QLineEdit, qApp, QFileDialog,QAction
from PyQt5.QtGui import QPixmap
import os
from PyQt5 import QtCore
from PyQt5 import QtWebEngineWidgets

if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
    qt_app = QtWidgets.QApplication(sys.argv)


class ANAEKRAN(QDialog):
    def __init__(self):
        super(ANAEKRAN, self).__init__()
        loadUi("yeniekran.ui", self)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        app.setStyle("fusion")
        
        self.baglanti_olustur()

        self.login.clicked.connect(self.loginbutton)
        self.register_2.clicked.connect(self.registerbutton)
    
    def baglanti_olustur(self):
        connection = sqlite3.connect("database.db")
        self.cursor = connection.cursor()
        connection.commit()
    
    def loginbutton(self):
        user = self.username.text()
        password = self.password.text()

        self.cursor.execute("Select * From uyegiris where username = ? and password = ?", (user, password))
        data = self.cursor.fetchall()

        if len(user) == 0 or len(password) == 0:
            self.error.setText("Please fill in all fields!")
        
        else:
            if len(data) == 0:
                self.error.setText("There is no such user!")
            else:
                data == password
                self.error.setText("")
                srch = searchengine()
                widget.addWidget(srch)
                widget.setCurrentIndex(widget.currentIndex()+1)

    def registerbutton(self):
        registersc = RegisterScreen()
        widget.addWidget(registersc)
        widget.setCurrentIndex(widget.currentIndex()+1)

class RegisterScreen(QDialog):
    def __init__(self):
        super(RegisterScreen, self).__init__()
        loadUi("kayitekrani.ui", self)
        self.createacc.clicked.connect(self.createaccount)
        self.back.clicked.connect(self.homescreen)

    def createaccount(self):
        user = self.username.text()
        passw = self.password.text()
        passw2 = self.password_2.text()

        if len(user) == 0 or len(passw) == 0 or len(passw2) == 0:
            self.error.setText("Please fill in all fields")
        elif passw != passw2:
            self.error.setText("Passwords do not match!")
        else:
            connection = sqlite3.connect("database.db")

            connection.execute("INSERT INTO uyegiris VALUES (?,?)", (user,passw))
            connection.commit()
            connection.close()
            srch = searchengine()
            widget.addWidget(srch)
            widget.setCurrentIndex(widget.currentIndex()+1)
        
    def homescreen(self):
        loginsc = ANAEKRAN()
        widget.addWidget(loginsc)
        widget.setCurrentIndex(widget.currentIndex()+1)

class searchengine(QDialog):
    def __init__(self):
        super(searchengine, self).__init__()
        loadUi("girisekrani.ui", self)
        
        
        self.google.clicked.connect(self.ggle)
        self.facebook.clicked.connect(self.fcbk)
        self.youtube.clicked.connect(self.ytb)
        self.twitter.clicked.connect(self.twt)
        self.instagram.clicked.connect(self.instag)
        self.reddit.clicked.connect(self.redt)
        self.amazon.clicked.connect(self.amazn)
        self.netflix.clicked.connect(self.netf)
        self.twitch.clicked.connect(self.twtch)
        
        
    def ggle(self):
        gogle = google()
        widget.addWidget(gogle)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def fcbk(self):
        face = facebook()
        widget.addWidget(face)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def ytb(self):
        ytbb= ytb()
        widget.addWidget(ytbb)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def twt(self):
        twtt = twitter()
        widget.addWidget(twtt)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def instag(self):
        ins = insta()
        widget.addWidget(ins)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def redt(self):
        red = reddit()
        widget.addWidget(red)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def amazn(self):
        amaz = amazon()
        widget.addWidget(amaz)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def netf(self):
        net = netflix()
        widget.addWidget(net)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def twtch(self):
        tw = twtch()
        widget.addWidget(tw)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    
        
class google(QDialog):
    def __init__(self):
        super(google, self).__init__()
        loadUi("google.ui", self)
        self.back.clicked.connect(self.bck)
        
        
    def bck(self):
        
        qApp.disconnect()
        srch = searchengine()
        widget.addWidget(srch)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
        
        
class facebook(QDialog):
    def __init__(self):
        super(facebook, self).__init__()
        loadUi("facebook.ui", self)
        self.back.clicked.connect(self.bck)
        
    def bck(self):
        srch = searchengine()
        widget.addWidget(srch)
        widget.setCurrentIndex(widget.currentIndex()+1)
class ytb(QDialog):
    def __init__(self):
        super(ytb, self).__init__()
        loadUi("youtube.ui", self)
        self.back.clicked.connect(self.bck)
        
    def bck(self):
        srch = searchengine()
        widget.addWidget(srch)
        widget.setCurrentIndex(widget.currentIndex()+1)
class twitter(QDialog):
    def __init__(self):
        super(twitter, self).__init__()
        loadUi("twitter.ui", self)
        self.back.clicked.connect(self.bck)
        
    def bck(self):
        srch = searchengine()
        widget.addWidget(srch)
        widget.setCurrentIndex(widget.currentIndex()+1)
class insta(QDialog):
    def __init__(self):
        super(insta, self).__init__()
        loadUi("instagram.ui", self)
        self.back.clicked.connect(self.bck)
        
    def bck(self):
        srch = searchengine()
        widget.addWidget(srch)
        widget.setCurrentIndex(widget.currentIndex()+1)
class reddit(QDialog):
    def __init__(self):
        super(reddit, self).__init__()
        loadUi("reddit.ui", self)
        self.back.clicked.connect(self.bck)
        
    def bck(self):
        srch = searchengine()
        widget.addWidget(srch)
        widget.setCurrentIndex(widget.currentIndex()+1)
class amazon(QDialog):
    def __init__(self):
        super(amazon, self).__init__()
        loadUi("amazon.ui", self)
        self.back.clicked.connect(self.bck)
        
    def bck(self):
        srch = searchengine()
        widget.addWidget(srch)
        widget.setCurrentIndex(widget.currentIndex()+1)
class netflix(QDialog):
    def __init__(self):
        super(netflix, self).__init__()
        loadUi("netflix.ui", self)
        self.back.clicked.connect(self.bck)
        
    def bck(self):
        srch = searchengine()
        widget.addWidget(srch)
        widget.setCurrentIndex(widget.currentIndex()+1)
class twtch(QDialog):
    def __init__(self):
        super(twtch, self).__init__()
        loadUi("twitch.ui", self)
        self.back.clicked.connect(self.bck)
        
    def bck(self):
        srch = searchengine()
        widget.addWidget(srch)
        widget.setCurrentIndex(widget.currentIndex()+1)


        
        

        

        
        
app = QApplication(sys.argv)
ana = ANAEKRAN()
widget = QStackedWidget()
widget.addWidget(ana)
widget.setFixedHeight(480)
widget.setFixedWidth(720)
widget.setWindowTitle("SABO")
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Çıkış Yapılıyor...")