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
        self.resize(pixmap.width(),pixmap.height())
        
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Fobby()
    sys.exit(app.exec_())
