#Welp, time to repurpose this abandoned repo 
#Switching from tkinter to pyqt 6 years later...

#Main Goal for this stage: Link widgets to varying datatypes

import os, os.path, random, re, pickle, atexit, sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class Fobby(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Fobby'
        self.left = 300
        self.top = 300
        self.width = 250
        self.height = 250
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        label = QLabel(self)
        pixmap = QPixmap('Fobby.gif')
        label.setPixmap(pixmap)
        #self.resize(pixmap.width(),pixmap.height())
        
        self.createGridLayout()

        #self.textbox = QLineEdit(self)
        #self.textbox.move(20, 20)
        #self.textbox.resize(280,40)
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.horizontalGroupBox)
        self.setLayout(windowLayout)
        self.show()
    
    def createGridLayout(self):
        self.horizontalGroupBox = QGroupBox("")
        layout = QGridLayout()
        layout.setColumnStretch(1, 4)
        layout.setColumnStretch(2, 4)

        layout.addWidget(QLabel('Let me identify what this is:'),0,0)
        layout.addWidget(QLineEdit(self),1,0)
        layout.addWidget(QLabel('Possible Datatype matches'),2,0)
        layout.addWidget(QLabel('Dunno, yet.'),3,0)
        
        self.horizontalGroupBox.setLayout(layout)
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Fobby()
    sys.exit(app.exec_())
