import PyQt5
import os, sys

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from child_window import ChildWindow
from page_one import page_one
from sign_up import signup



class Main:
    def __init__(self):
        self.show_page_sign_up()
        pass
    
    
    def show_page_sign_up(self):
        fob = open('data.txt','r')
        data =fob.read()
        fob.close()
        if data == '':
            self.signup= signup()
            self.signup.switch_window.connect(self.show_child)
            self.signup.show()
        else:
            self.show_page_one()
    
    
    def show_page_one(self):
        
        self.page_one = page_one()
        self.page_one.switch_window.connect(self.show_child)
        self.page_one.show()
        return
    
    def show_child(self):
        self.child = ChildWindow()
        self.child.switch_window.connect(self.show_page_one)
        self.page_one.close()
        self.child.show()











 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Main()
    sys.exit(app.exec_())