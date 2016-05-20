from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class dino(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(500,500,600,300)
        self.grid=QGridLayout()

        self.picture1=QPixmap("1.jpg")
        self.picture2=QPixmap("2.jpg")
        self.picture3=QPixmap("3.jpg")
        self.picture4=QPixmap("4.jpg")

        self.lbl1=QLabel(self)
        self.lbl1.setPixmap(self.picture1)
        self.lbl2=QLabel(self)
        self.lbl2.setPixmap(self.picture2)
        self.lbl3=QLabel(self)
        self.lbl3.setPixmap(self.picture3)
        self.lbl4=QLabel(self)
        self.lbl4.setPixmap(self.picture4)
