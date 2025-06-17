#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import math
import random
import numpy as np
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, 
                           QMessageBox, QGraphicsScene, QGraphicsView, 
                           QGraphicsLineItem, QGraphicsTextItem, QVBoxLayout, 
                           QHBoxLayout, QGridLayout)
from PyQt5.QtCore import Qt, pyqtSignal, QPointF
from PyQt5.QtGui import QPen, QFont, QPainter

from dialog import Dialog
from engine import Engine

class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
        
        # 初始化实例变量
        self.A = 0
        self.C = 0
        self.enginetype = 0
        
        # 计算所需的变量
        self.wp = 0              # 有效载荷 kg
        self.vcc = 0             # 巡航速度 m/h
        self.heightcc = 0        # 巡航高度 m
        self.standbyoil = 0      # 飞行待机用油 min
        self.takelength = 0      # 起飞场长 m
        self.landlength = 0      # 着陆场长 m
        self.R = 0               # 航程 km
        self.sfc = 0             # 巡航耗油率 kg/kw/s
        self.clmax = 0           # 最大升力系数 C_lmax
        self.vv = 0              # 设计爬升率 m/s
        self.vs = 0              # 失速速度 m/s
        self.initialwto = 0      # 初始估算重量 kg
        self.lnd = 0             # 升阻比
        self.ar = 0              # 展弦比
        self.perfuel = 0         # 燃油系数
        self.qcc = 0
        self.cdmin = 0
        self.k = 0
        self.n = 0
        self.qtl = 0
    
    def initUI(self):
        # 设置窗口属性
        self.setWindowTitle("飞机边界线图绘制软件")
        self.setGeometry(100, 100, 1259, 658)
        
        # 创建布局
        mainLayout = QVBoxLayout()
        
        # 第一行 - 有效载荷、巡航速度、巡航高度、飞行待机用油、航程
        row1 = QHBoxLayout()
        
        # 有效载荷
        row1.addWidget(self.createLabel("有效载荷（kg）"))
        self.lineEdit_1 = QLineEdit()
        row1.addWidget(self.lineEdit_1)
        
        # 巡航速度
        row1.addWidget(self.createLabel("巡航速度（m/h）"))
        self.lineEdit_2 = QLineEdit()
        row1.addWidget(self.lineEdit_2)
        
        # 巡航高度
        row1.addWidget(self.createLabel("巡航高度（m）"))
        self.lineEdit_3 = QLineEdit()
        row1.addWidget(self.lineEdit_3)
        
        # 飞行待机用油
        row1.addWidget(self.createLabel("飞行待机用油（s）"))
        self.lineEdit_5 = QLineEdit()
        row1.addWidget(self.lineEdit_5)
        
        # 航程
        row1.addWidget(self.createLabel("航程（km）"))
        self.lineEdit_10 = QLineEdit()
        row1.addWidget(self.lineEdit_10)
        
        mainLayout.addLayout(row1)
        
        # 第二行 - 起飞场长、着陆场长等
        row2 = QHBoxLayout()
        
        # 起飞场长
        row2.addWidget(self.createLabel("起飞场长（m）"))
        self.lineEdit_6 = QLineEdit()
        row2.addWidget(self.lineEdit_6)
        
        # 着陆场长
        row2.addWidget(self.createLabel("着陆场长（m）"))
        self.lineEdit_7 = QLineEdit()
        row2.addWidget(self.lineEdit_7)
        
        # 巡航耗油率
        row2.addWidget(self.createLabel("巡航耗油率"))
        self.lineEdit_11 = QLineEdit()
        row2.addWidget(self.lineEdit_11)
        
        # 最大升力系数
        row2.addWidget(self.createLabel("最大升力系数"))
        self.lineEdit_12 = QLineEdit()
        row2.addWidget(self.lineEdit_12)
        
        mainLayout.addLayout(row2)
        
        # 第三行 - 设计爬升率、失速速度、初始估算重量
        row3 = QHBoxLayout()
        
        # 设计爬升率
        row3.addWidget(self.createLabel("设计爬升率（m/s）"))
        self.lineEdit_13 = QLineEdit()
        row3.addWidget(self.lineEdit_13)
        
        # 失速速度
        row3.addWidget(self.createLabel("失速速度（m/s）"))
        self.lineEdit_14 = QLineEdit()
        row3.addWidget(self.lineEdit_14)
        
        # 初始估算重量
        row3.addWidget(self.createLabel("初始估算重量（kg）"))
        self.lineEdit_15 = QLineEdit()
        row3.addWidget(self.lineEdit_15)
        
        # 升阻比
        row3.addWidget(self.createLabel("升阻比"))
        self.lineEdit_18 = QLineEdit()
        row3.addWidget(self.lineEdit_18)
        
        # 展弦比
        row3.addWidget(self.createLabel("展弦比"))
        self.lineEdit_20 = QLineEdit()
        row3.addWidget(self.lineEdit_20)
        
        mainLayout.addLayout(row3)
        
        # 第四行 - 选择按钮
        row4 = QHBoxLayout()
        
        self.pushButton = QPushButton("选择飞机类型")
        self.pushButton.clicked.connect(self.openDialog)
        row4.addWidget(self.pushButton)
        
        self.pushButton2 = QPushButton("选择发动机类型")
        self.pushButton2.clicked.connect(self.openEngine)
        row4.addWidget(self.pushButton2)
        
        self.pushButton_2 = QPushButton("计算")
        self.pushButton_2.clicked.connect(self.onCalculateClicked)
        row4.addWidget(self.pushButton_2)
        
        mainLayout.addLayout(row4)
        
        # 添加图形视图
        self.graphicsView = QGraphicsView()
        self.graphicsView.setMinimumSize(800, 400)
        mainLayout.addWidget(self.graphicsView)
        
        self.setLayout(mainLayout)
        
        # 创建对话框
        self.mydialog = Dialog(self)
        self.mydialog.sendData.connect(self.receiveData)
        
        self.myengine = Engine(self)
        self.myengine.sendData.connect(self.receiveEngineData)
    
    def createLabel(self, text):
        label = QLabel(f"<html><head/><body><p><span style=\" font-size:16pt;\">{text}</span></p></body></html>")
        label.setAlignment(Qt.AlignLeading | Qt.AlignLeft | Qt.AlignVCenter)
        return label
    
    def openDialog(self):
        self.mydialog.show()
    
    def receiveData(self, a, c, buttonText):
        self.A = a
        self.C = c
        self.pushButton.setText(buttonText)
    
    def openEngine(self):
        self.myengine.show()
    
    def receiveEngineData(self, enginetype, buttonText):
        self.enginetype = enginetype
        self.pushButton2.setText(buttonText)
    
    def plotCurve(self, qcc, cdmin, k, densitycc, vs, takelength, landlength, vv, qtl, clmax):
        scene = QGraphicsScene(self)
        self.graphicsView.setScene(scene)
        self.graphicsView.setRenderHint(QPainter.Antialiasing)
        self.graphicsView.setSceneRect(0, -200, 400, 200)
        
        step = 0.1
        xStart = 0.0
        xEnd = 120.0
        
        scaleX = 2.0
        scaleY = 300
        
        lastPoint2 = None
        lastPoint3 = None
        lastPoint4 = None
        lastPoint5 = None
        
        for x in np.arange(xStart, xEnd + step, step):
            y2 = (vv) / (2 * x * math.sqrt(k / (3 * cdmin)) / 1.225) + (cdmin / x) + (k * x / qtl)
            y3 = (1.1 * vs) * (1.1 * vs) / 2 / 9.81 / takelength + qtl * 0.0425 / x + 0.04 - 0.04 * qtl * 0.7 / x
            y4 = qtl * cdmin / x + k * x / qtl
            y5 = 0.01 * self.vcc / (2 * x * math.sqrt(k / (3 * cdmin)) / densitycc) + 4 * math.sqrt(k * cdmin / 3)
            
            point2 = QPointF(x * scaleX, -y2 * scaleY)
            point3 = QPointF(x * scaleX, -y3 * scaleY)
            point4 = QPointF(x * scaleX, -y4 * scaleY)
            point5 = QPointF(x * scaleX, -y5 * scaleY)
            
            if lastPoint2:
                scene.addLine(QPointF(lastPoint2.x(), lastPoint2.y()), 
                             QPointF(point2.x(), point2.y()), 
                             QPen(Qt.red))
                scene.addLine(QPointF(lastPoint3.x(), lastPoint3.y()), 
                             QPointF(point3.x(), point3.y()), 
                             QPen(Qt.green))
                scene.addLine(QPointF(lastPoint4.x(), lastPoint4.y()), 
                             QPointF(point4.x(), point4.y()), 
                             QPen(Qt.blue))
                scene.addLine(QPointF(lastPoint5.x(), lastPoint5.y()), 
                             QPointF(point5.x(), point5.y()), 
                             QPen(Qt.red))
            
            lastPoint2 = point2
            lastPoint3 = point3
            lastPoint4 = point4
            lastPoint5 = point5
        
        # 绘制特殊线条
        x_target = 0.5 * clmax * 1.225 * vs * vs
        x_target2 = 1.225 * clmax * (landlength - 183) / 5
        
        scene.addLine(x_target * scaleX, -200, x_target * scaleX, 0, 
                     QPen(Qt.black, 2, Qt.DashLine))
        scene.addLine(x_target2 * scaleX, -200, x_target2 * scaleX, 0, 
                     QPen(Qt.red, 2, Qt.DashLine))
        
        # 绘制坐标轴
        scene.addLine(0, 0, 400, 0, QPen(Qt.black))  # x轴
        scene.addLine(0, 0, 0, -200, QPen(Qt.black))  # y轴
        
        # 添加刻度
        font = QFont()
        font.setPointSize(8)
        
        # x轴刻度
        for i in range(0, 121, 20):
            scene.addLine(i * scaleX, 0, i * scaleX, -5, QPen(Qt.black))
            text = QGraphicsTextItem(str(i))
            text.setFont(font)
            text.setPos(i * scaleX - 10, 5)
            scene.addItem(text)
        
        # y轴刻度
        for i in range(0, 201, 20):
            scene.addLine(0, -i, 5, -i, QPen(Qt.black))
            text = QGraphicsTextItem(str(i / scaleY))
            text.setFont(font)
            text.setPos(-25, -i - 8)
            scene.addItem(text)
    
    def onCalculateClicked(self):
        ok = True
        
        def getFloatFromLineEdit(edit, warning):
            nonlocal ok
            try:
                value = float(edit.text())
                return value
            except ValueError:
                QMessageBox.warning(self, "输入错误", warning)
                ok = False
                return 0.0
        
        # 获取输入值
        self.wp = getFloatFromLineEdit(self.lineEdit_1, "请输入有效的有效载荷喵！")
        self.vcc = getFloatFromLineEdit(self.lineEdit_2, "请输入有效的巡航速度喵！")
        self.heightcc = getFloatFromLineEdit(self.lineEdit_3, "请输入有效的巡航高度喵！")
        self.standbyoil = getFloatFromLineEdit(self.lineEdit_5, "请输入有效的飞行待机用油喵！")
        self.takelength = getFloatFromLineEdit(self.lineEdit_6, "请输入有效的起飞场长喵！")
        self.landlength = getFloatFromLineEdit(self.lineEdit_7, "请输入有效的着陆场长喵！")
        self.R = getFloatFromLineEdit(self.lineEdit_10, "请输入有效的航程喵！")
        self.sfc = getFloatFromLineEdit(self.lineEdit_11, "请输入有效的巡航耗油率喵！")
        self.clmax = getFloatFromLineEdit(self.lineEdit_12, "请输入有效的最大升力系数喵！")
        self.vv = getFloatFromLineEdit(self.lineEdit_13, "请输入有效的设计爬升率喵！")
        self.vs = getFloatFromLineEdit(self.lineEdit_14, "请输入有效的失速速度喵！")
        self.initialwto = getFloatFromLineEdit(self.lineEdit_15, "请输入有效的初始估算重量喵！")
        self.lnd = getFloatFromLineEdit(self.lineEdit_18, "请输入有效的升阻比喵！")
        self.ar = getFloatFromLineEdit(self.lineEdit_20, "请输入有效的展弦比喵！")
        
        if not ok:
            return
        
        # 计算燃油系数
        E = self.standbyoil / 100.0
        rnd1 = 0.97 + (0.975 - 0.97) * random.random()  # 起飞重量调整因子
        rnd2 = 0.990 + (0.995 - 0.990) * random.random()  # 飞行任务调整因子
        rnd3 = 0.992 + (0.997 - 0.992) * random.random()  # 备降调整因子
        
        term1 = math.exp(-self.R * self.sfc / self.vcc / self.lnd)
        term2 = math.exp(-E * self.sfc / self.lnd)
        self.perfuel = 1.06 * (1 - rnd1 * 0.985 * term1 * term2 * rnd2 * rnd3)
        
        # 计算空重系数
        perempty = self.A * math.pow(self.initialwto, self.C)
        wto = self.initialwto
        error = 1.0
        maxIterations = 1000
        iteration = 0
        
        while error > 1e-6 and iteration < maxIterations:
            denominator = 1 - perempty - self.perfuel
            if denominator <= 0:
                QMessageBox.warning(self, "计算错误", "分母为0或负数，无法计算喵！")
                return
            
            wto = self.wp / denominator
            error = abs((wto - self.initialwto) / wto)
            self.initialwto = wto
            iteration += 1
        
        if iteration >= maxIterations:
            QMessageBox.warning(self, "计算错误", "最大起飞重量迭代未收敛喵！")
            return
        
        # 计算界限线图参数
        densitycc = 1.225 * math.pow((1 - 0.0065 * self.heightcc / 288.15), 4.25588)  # 标准大气模型
        self.cdmin = 0.0325
        self.k = 1.0 / (math.pi * 0.8 * self.ar)
        self.qcc = 0.5 * densitycc * self.vcc * self.vcc
        self.qtl = 0.5 * 1.225 * 1.21 * self.vs * self.vs
        
        # 绘制界限线图
        self.plotCurve(self.qcc, self.cdmin, self.k, densitycc, self.vs, 
                      self.takelength, self.landlength, self.vv, self.qtl, self.clmax) 