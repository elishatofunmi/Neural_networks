import PyQt5
import os, sys
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import tensorflow as tf
import keras
from keras.models import load_model
from keras.preprocessing import image



class ChildWindow(QWidget):
    switch_window = pyqtSignal()
    
    def __init__(self, parent = None):
        super(ChildWindow, self).__init__(parent)


        self.setWindowTitle('Breast Cancer Classification')
        self.setGeometry(100,100,700,500)
        self.setMaximumSize(700,500)
        
        # initialize the grid layout
        
        
        layout = QBoxLayout(QBoxLayout.LeftToRight)
        layout3 = QBoxLayout(QBoxLayout.LeftToRight)
        layout2 = QBoxLayout(QBoxLayout.TopToBottom)
        
        
        layout2.addLayout(layout)
        layout2.addLayout(layout3)
        
        
        
        # initialize the background image
        qimage = QImage(r"C:\Users\user\Desktop\Dataset_BUSI\breast cancer\images.jpeg")
        simage = qimage.scaled(QSize(700,500))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(simage))
        self.setPalette(palette)
        
        
        
        
        # image
        
        
        self.update_label = QLabel(self)
        update_image = QPixmap(r"C:\Users\user\Desktop\Dataset_BUSI\breast cancer\class_image.png")
        self.update_label.setPixmap(update_image)
        self.update_label.setFixedSize(QSize(300,300))
        
        layout.addWidget(self.update_label,0)
        
        space_label = QLabel('')
        space_label.setFixedSize(QSize(20,100))
        layout.addWidget(space_label, 0)
        
        
        self.update_label_one = QLabel('')
        #update_image_one = QPixmap(r"C:\Users\user\Desktop\Dataset_BUSI\breast cancer\class_image.png")
        #self.update_label_one.setPixmap(update_image_one)
        self.update_label_one.setFixedSize(QSize(300,300))
        
        layout.addWidget(self.update_label_one,0)
        
        
        #select image
        select_image = QPushButton('Select Image')
        layout3.addWidget(select_image, 1)
        select_image.clicked.connect(self.get_image)
        select_image.setFixedSize(QSize(120,30))
        
        # push button
        login_pushbutton = QPushButton('analyze')
        layout3.addWidget(login_pushbutton,1)
        login_pushbutton.clicked.connect(self.analyze_button)
        login_pushbutton.setFixedSize(QSize(120,30))
        
        
        # cancel button
        
        cancel_pushbutton = QPushButton('exit')
        layout3.addWidget(cancel_pushbutton, 1)
        cancel_pushbutton.clicked.connect(self.exit_button)
        cancel_pushbutton.setFixedSize(QSize(120,30))
        
        
        self.setLayout(layout2)
        self.classification_file = None

        self.show()
        
        
        return
    
    def get_image(self):
        filedialog = QFileDialog.Options()
        filedialog = QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self,'QFileDialog.getOpenFileName()', "","All Files (*.png)", options = filedialog)
        if filename:
            self.classification_file = filename
            update_image_two = QPixmap(filename)
            self.update_label.setPixmap(update_image_two)
            self.update_label.setFixedSize(QSize(300,300))
        else:
            pass
        return
    
    def analyze_button(self):
        #load model using keras
        model = load_model('breast_cancer.h5')
        img = image.load_img(self.classification_file, target_size = (200,150,3), grayscale = False)
        img=image.img_to_array(img)
        img = img/255
        img = img.reshape((1,200,150,3))
        value = model.predict(img)
        
        round_up = np.round(value)[0]
        
        count , value= 0,0
        for k in round_up:
            if k == 1.0:
                value = count
                break
            else:
                count += 1

        if value == 0:
            file_dir = r"C:\Users\user\Desktop\Dataset_BUSI\breast cancer\benign.PNG"
            update_image_two = QPixmap(file_dir)
            self.update_label_one.setPixmap(update_image_two)
            self.update_label_one.setFixedSize(QSize(300,300))
        elif value == 1:
            file_dir = r"C:\Users\user\Desktop\Dataset_BUSI\breast cancer\malignant.PNG"
            update_image_two = QPixmap(file_dir)
            self.update_label_one.setPixmap(update_image_two)
            self.update_label_one.setFixedSize(QSize(300,300))
        else:
            file_dir = r"C:\Users\user\Desktop\Dataset_BUSI\breast cancer\normal.PNG"
            update_image_two = QPixmap(file_dir)
            self.update_label_one.setPixmap(update_image_two)
            self.update_label_one.setFixedSize(QSize(300,300))

        
        return
    
    
    def exit_button(self):
        self.switch_window.emit()
        return 
    
    
    
    

#if __name__ == '__main__':
#    app = QApplication(sys.argv)
#    main = ChildWindow()
#    main.show()
#    sys.exit(app.exec_())