#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import pyqtSignal

class Dialog(QDialog):
    # 创建信号
    sendData = pyqtSignal(float, float, str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("选择飞机类型")
        self.setGeometry(300, 300, 302, 190)
        
        # 创建布局
        mainLayout = QVBoxLayout()
        topRow = QHBoxLayout()
        bottomRow = QHBoxLayout()
        
        # 创建按钮
        self.button1 = QPushButton("通航飞机（单发）")
        self.button2 = QPushButton("通航飞机（双发）")
        self.button3 = QPushButton("农用飞机")
        self.button4 = QPushButton("双发涡桨飞机")
        
        # 连接信号和槽
        self.button1.clicked.connect(self.on_button1_clicked)
        self.button2.clicked.connect(self.on_button2_clicked)
        self.button3.clicked.connect(self.on_button3_clicked)
        self.button4.clicked.connect(self.on_button4_clicked)
        
        # 添加按钮到布局
        topRow.addWidget(self.button1)
        topRow.addWidget(self.button2)
        bottomRow.addWidget(self.button3)
        bottomRow.addWidget(self.button4)
        
        mainLayout.addLayout(topRow)
        mainLayout.addLayout(bottomRow)
        
        self.setLayout(mainLayout)
    
    def on_button1_clicked(self):
        self.sendData.emit(2.05, -0.18, self.button1.text())
        self.close()
    
    def on_button2_clicked(self):
        self.sendData.emit(1.4, -0.10, self.button2.text())
        self.close()
    
    def on_button3_clicked(self):
        self.sendData.emit(0.72, -0.03, self.button3.text())
        self.close()
    
    def on_button4_clicked(self):
        self.sendData.emit(0.92, -0.05, self.button4.text())
        self.close() 