from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui
import sys
import random
import sqlite3


class my_window(QWidget):

    def __init__(self):
        super().__init__()
        self.conn=sqlite3.connect('sdu_eng.db')
        self.query='''
              CREATE TABLE STUDENTS ( NAME TEXT NOT NULL,
                                     SURNAME TEXT NOT NULL
                                     );'''

        self.setGeometry(100,100,500,200)
        self.setWindowTitle("Test windows")

        self.name=QLabel("Enter your name",self)
        self.name.move(5,10)

        self.name_input=QLineEdit(self)
        self.name_input.move(120,10)

        self.name=QLabel("Enter your surname",self)
        self.name.move(5,50)

        self.surname_input=QLineEdit(self)
        self.surname_input.move(150,45)

        self.btn=QPushButton("Log in",self)
        self.btn.move(260,150)

        self.button=QPushButton("Registration",self)
        self.button.move(360,150)

        self.button.clicked.connect(self.reg)

        self.btn.clicked.connect(self.say_hello)
        self.show()

    def reg(self):
        self.s=self.name_input.text()
        self.c=self.surname_input.text()
        reg=''' INSERT INTO STUDENTS VALUES (%s,%s);''',(self.s,self.c)

        show=''' select * from STUDENTS;'''
        self.conn.execute(reg)
        self.conn.commit()


    def say_hello(self):
        self.l=0
        k=self.l
        s=self.name_input.text()
        c=self.surname_input.text()
        self.p=s+c
        o=self.p

        openedFile = open('name','r')
        txt=openedFile.read()
        r=txt.split()
        for i in r:
            if i==o:
               QMessageBox.information(self,"Log in","Welcome")
               self.close()
               break
            else:
               k+=1
               if k==len(r):
                  QMessageBox.information(self,"Log in","wrong name or surname")
                  self.close()
                  break


app=QApplication(sys.argv)
test=my_window()
sys.exit(app.exec_())
