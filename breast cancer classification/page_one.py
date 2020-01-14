import PyQt5
import os, sys

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *



class page_one(QWidget):
    switch_window = pyqtSignal(str)
    
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle('Breast Cancer Classification')
        self.setGeometry(100,100,700,500)
        self.setMaximumSize(700,500)
        
        
        # initialize the grid layout
        layout = QGridLayout()
        self.setLayout(layout)
        
        # initialize the background image
        qimage = QImage(r"C:\Users\user\Desktop\Dataset_BUSI\breast cancer\images.jpeg")
        simage = qimage.scaled(QSize(700,500))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(simage))
        self.setPalette(palette)
        
        
        
        #dummy labels
        dummy_one = QLabel('')
        layout.addWidget(dummy_one, 0,0,1,1)
        
        dummy_two = QLabel('')
        layout.addWidget(dummy_two, 9,0,1,14)

        
        
        # the login boxes
        # labels
        username_label = QLabel('USERNAME:')
        layout.addWidget(username_label, 4,3)
        
        password_label = QLabel('PASSWORD:')
        layout.addWidget(password_label, 6,3)
        
        # input boxes
        # username
        self.username_lineedit = QLineEdit()
        layout.addWidget(self.username_lineedit,4,5,1,5)
        
        # password
        self.password_lineedit = QLineEdit()
        self.password_lineedit.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.password_lineedit, 6,5,1,5)
        
        # push button
        login_pushbutton = QPushButton('LOGIN')
        layout.addWidget(login_pushbutton,8,6)
        login_pushbutton.clicked.connect(self.login_button)
        
        
        # cancel button
        
        cancel_pushbutton = QPushButton('CANCEL')
        layout.addWidget(cancel_pushbutton, 8,8)
        cancel_pushbutton.clicked.connect(self.cancel_button)
        
        self.show()
        
        return
    
    def login_button(self):
        fob = open('data.txt', 'r')
        targ = fob.read()
        fob.close()
        if self.password_lineedit.text() == targ:
            self.switch_window.emit(self.username_lineedit.text())
        else:
            pass
        return
    
    
    def cancel_button(self):
        sys.exit()
        return
    
    
    
 
#
#if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    main = page_one()
#    main.show()
#    sys.exit(app.exec_())