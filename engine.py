#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QDialog, QPushButton, QVBoxLayout
from PyQt5.QtCore import pyqtSignal

class Engine(QDialog):
    # 创建信号
    sendData = pyqtSignal(int, str)
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("选择发动机类型")
        self.setGeometry(300, 300, 186, 173)
        
        # 创建布局
        layout = QVBoxLayout()
        
        # 创建按钮
        self.pushButton1 = QPushButton("活塞")
        self.pushButton2 = QPushButton("涡桨")
        
        # 连接信号和槽
        self.pushButton1.clicked.connect(self.on_pushButton1_clicked)
        self.pushButton2.clicked.connect(self.on_pushButton2_clicked)
        
        # 添加按钮到布局
        layout.addWidget(self.pushButton1)
        layout.addWidget(self.pushButton2)
        
        self.setLayout(layout)
    
    def on_pushButton1_clicked(self):
        self.sendData.emit(1, self.pushButton1.text())
        self.close()
    
    def on_pushButton2_clicked(self):
        self.sendData.emit(2, self.pushButton2.text())
        self.close() 