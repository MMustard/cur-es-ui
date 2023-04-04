# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#

from model import inference
import os
from typing import Dict, List
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PIL import Image
import gdapi


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1514, 796)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("titleicon.png"),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color:rgb(57, 60, 67);\n"
                                 "color: rgb(255, 255, 255);\n"
                                 "background-color: rgb(40, 40, 47)\n"
                                 ";")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 351, 71))
        font = QtGui.QFont()
        font.setFamily("FangSong")
        self.label.setFont(font)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setPixmap(QtGui.QPixmap("北交校徽-红色.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(530, 10, 611, 61))
        font = QtGui.QFont()
        font.setFamily("华文中宋")
        font.setPointSize(36)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setTextFormat(QtCore.Qt.AutoText)
        self.label_2.setScaledContents(False)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 190, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_output = QtWidgets.QLabel(self.centralwidget)
        self.label_output.setGeometry(QtCore.QRect(500, 190, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(18)
        self.label_output.setFont(font)
        self.label_output.setObjectName("label_output")
        self.inputImage = QtWidgets.QLabel(self.centralwidget)
        self.inputImage.setGeometry(QtCore.QRect(40, 240, 320, 320))
        font = QtGui.QFont()
        font.setFamily("FangSong")
        self.inputImage.setFont(font)
        self.inputImage.setStyleSheet("\n"
                                      "border-style:solid;\n"
                                      "border-color: rgb(0, 0, 0);\n"
                                      "border-width: 7px;\n"
                                      "border-style: solid;\n"
                                      "background-color: rgb(100, 149, 237);")
        self.inputImage.setText("")
        self.inputImage.setPixmap(QtGui.QPixmap("2.jpg"))
        self.inputImage.setScaledContents(True)
        self.inputImage.setIndent(-1)
        self.inputImage.setObjectName("inputImage")
        self.label_GT = QtWidgets.QLabel(self.centralwidget)
        self.label_GT.setGeometry(QtCore.QRect(870, 190, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(18)
        self.label_GT.setFont(font)
        self.label_GT.setObjectName("label_GT")
        self.GT = QtWidgets.QLabel(self.centralwidget)
        self.GT.setGeometry(QtCore.QRect(740, 240, 320, 320))
        font = QtGui.QFont()
        font.setFamily("FangSong")
        self.GT.setFont(font)
        self.GT.setStyleSheet("\n"
                              "border-style:solid;\n"
                              "border-color: rgb(0, 0, 0);\n"
                              "border-width: 7px;\n"
                              "border-style: solid;\n"
                              "background-color: rgb(100, 149, 237);")
        self.GT.setText("")
        self.GT.setPixmap(QtGui.QPixmap("2.png"))
        self.GT.setScaledContents(True)
        self.GT.setObjectName("GT")
        self.selectInput = QtWidgets.QPushButton(self.centralwidget)
        self.selectInput.setGeometry(QtCore.QRect(60, 580, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.selectInput.setFont(font)
        self.selectInput.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.selectInput.setMouseTracking(False)
        self.selectInput.setStyleSheet("\n"
                                       "border-style:solid;\n"
                                       "border-color: rgb(0, 0, 0);\n"
                                       "border-width: 5px;\n"
                                       "border-radius: 10px;\n"
                                       "background-color: rgb(150, 150, 150);")
        self.selectInput.setObjectName("selectInput")
        self.inputImagePath = QtWidgets.QLabel(self.centralwidget)
        self.inputImagePath.setGeometry(QtCore.QRect(390, 600, 461, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.inputImagePath.setFont(font)
        self.inputImagePath.setObjectName("inputImagePath")
        self.outputImage = QtWidgets.QLabel(self.centralwidget)
        self.outputImage.setGeometry(QtCore.QRect(390, 240, 320, 320))
        font = QtGui.QFont()
        font.setFamily("FangSong")
        self.outputImage.setFont(font)
        self.outputImage.setStyleSheet("\n"
                                       "border-style:solid;\n"
                                       "border-color: rgb(0, 0, 0);\n"
                                       "border-width: 7px;\n"
                                       "border-style: solid;\n"
                                       "background-color: rgb(100, 149, 237);")
        self.outputImage.setText("")
        self.outputImage.setPixmap(QtGui.QPixmap("2.png"))
        self.outputImage.setScaledContents(True)
        self.outputImage.setObjectName("outputImage")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(210, 700, 821, 23))
        font = QtGui.QFont()
        font.setFamily("FangSong")
        self.progressBar.setFont(font)
        self.progressBar.setCursor(QtGui.QCursor(QtCore.Qt.WaitCursor))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 150, 521, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(63, 63, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(80, 80, 80))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ToolTipText, brush)
        self.line.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("FangSong")
        self.line.setFont(font)
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet("\n"
                                "\n"
                                "border-width: 3px;\n"
                                "border-style: solid;\n"
                                "border-color: rgb(80, 80,80);\n"
                                "background-color: rgb(80, 80, 80);")
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(1110, 160, 20, 601))
        font = QtGui.QFont()
        font.setFamily("FangSong")
        self.line_2.setFont(font)
        self.line_2.setStyleSheet("\n"
                                  "\n"
                                  "border-width: 3px;\n"
                                  "border-style: solid;\n"
                                  "border-color: rgb(80, 80,80);\n"
                                  "background-color: rgb(80, 80, 80);")
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(0, 100, 511, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.label_7.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("\n"
                                   "border-style:solid;\n"
                                   "border-color: rgb(0, 0, 0);\n"
                                   "border-width: 5px;\n"
                                   "border-radius: 5px;\n"
                                   "background-color: rgb(40, 40, 47);")
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(520, 150, 521, 16))
        font = QtGui.QFont()
        font.setFamily("FangSong")
        self.line_3.setFont(font)
        self.line_3.setStyleSheet("\n"
                                  "\n"
                                  "border-width: 3px;\n"
                                  "border-style: solid;\n"
                                  "border-color: rgb(80, 80,80);\n"
                                  "background-color: rgb(80, 80, 80);")
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(510, 100, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_8.setFont(font)
        self.label_8.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.label_8.setStyleSheet("\n"
                                   "border-style:solid;\n"
                                   "border-color: rgb(0, 0, 0);\n"
                                   "border-width: 5px;\n"
                                   "border-radius: 5px;\n"
                                   "background-color: rgb(40, 40, 47);")
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(1040, 150, 521, 16))
        font = QtGui.QFont()
        font.setFamily("FangSong")
        self.line_4.setFont(font)
        self.line_4.setStyleSheet("\n"
                                  "\n"
                                  "border-width: 3px;\n"
                                  "border-style: solid;\n"
                                  "border-color: rgb(80, 80,80);\n"
                                  "background-color: rgb(80, 80,80);")
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.saveOutput = QtWidgets.QPushButton(self.centralwidget)
        self.saveOutput.setGeometry(QtCore.QRect(210, 580, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.saveOutput.setFont(font)
        self.saveOutput.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.saveOutput.setMouseTracking(False)
        self.saveOutput.setStyleSheet("\n"
                                      "border-style:solid;\n"
                                      "border-color: rgb(0, 0, 0);\n"
                                      "border-width: 5px;\n"
                                      "border-radius: 10px;\n"
                                      "background-color: rgb(150, 150, 150);")
        self.saveOutput.setAutoRepeatInterval(99)
        self.saveOutput.setAutoDefault(True)
        self.saveOutput.setDefault(True)
        self.saveOutput.setObjectName("saveOutput")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(1270, 180, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(1170, 290, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.IoU_baseline = QtWidgets.QLineEdit(self.centralwidget)
        self.IoU_baseline.setGeometry(QtCore.QRect(1280, 300, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.IoU_baseline.setFont(font)
        self.IoU_baseline.setStyleSheet("border-width: 0px;\n"
                                        "border-style: solid;\n"
                                        "")
        self.IoU_baseline.setReadOnly(True)
        self.IoU_baseline.setCursorMoveStyle(QtCore.Qt.LogicalMoveStyle)
        self.IoU_baseline.setObjectName("IoU_baseline")
        self.PA_baseline = QtWidgets.QLineEdit(self.centralwidget)
        self.PA_baseline.setGeometry(QtCore.QRect(1270, 370, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.PA_baseline.setFont(font)
        self.PA_baseline.setStyleSheet("border-width: 0px;\n"
                                       "border-style: solid;\n"
                                       "")
        self.PA_baseline.setReadOnly(True)
        self.PA_baseline.setObjectName("PA_baseline")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(1170, 370, 51, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label_19.setFont(font)
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(1170, 450, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.MAE_baseline = QtWidgets.QLineEdit(self.centralwidget)
        self.MAE_baseline.setGeometry(QtCore.QRect(1270, 450, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.MAE_baseline.setFont(font)
        self.MAE_baseline.setStyleSheet("border-width: 0px;\n"
                                        "border-style: solid;\n"
                                        "")
        self.MAE_baseline.setReadOnly(True)
        self.MAE_baseline.setObjectName("MAE_baseline")
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(1170, 530, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.label_21.setFont(font)
        self.label_21.setObjectName("label_21")
        self.PA_ours = QtWidgets.QLineEdit(self.centralwidget)
        self.PA_ours.setGeometry(QtCore.QRect(1390, 370, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.PA_ours.setFont(font)
        self.PA_ours.setStyleSheet("border-width: 0px;\n"
                                   "border-style: solid;\n"
                                   "")
        self.PA_ours.setReadOnly(True)
        self.PA_ours.setObjectName("PA_ours")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(1270, 240, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        self.label_15.setFont(font)
        self.label_15.setTextFormat(QtCore.Qt.PlainText)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(1390, 240, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.IoU_ours = QtWidgets.QLineEdit(self.centralwidget)
        self.IoU_ours.setGeometry(QtCore.QRect(1400, 290, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.IoU_ours.setFont(font)
        self.IoU_ours.setStyleSheet("border-width: 0px;\n"
                                    "border-style: solid;\n"
                                    "")
        self.IoU_ours.setReadOnly(True)
        self.IoU_ours.setObjectName("IoU_ours")
        self.MAE_ours = QtWidgets.QLineEdit(self.centralwidget)
        self.MAE_ours.setEnabled(True)
        self.MAE_ours.setGeometry(QtCore.QRect(1390, 450, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.MAE_ours.setFont(font)
        self.MAE_ours.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.MAE_ours.setStyleSheet("border-width: 0px;\n"
                                    "border-style: solid;\n"
                                    "")
        self.MAE_ours.setReadOnly(True)
        self.MAE_ours.setObjectName("MAE_ours")
        self.BER_baseline = QtWidgets.QLineEdit(self.centralwidget)
        self.BER_baseline.setGeometry(QtCore.QRect(1270, 530, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.BER_baseline.setFont(font)
        self.BER_baseline.setStyleSheet("border-width: 0px;\n"
                                        "border-style: solid;\n"
                                        "")
        self.BER_baseline.setReadOnly(True)
        self.BER_baseline.setObjectName("BER_baseline")
        self.BER_ours = QtWidgets.QLineEdit(self.centralwidget)
        self.BER_ours.setGeometry(QtCore.QRect(1390, 530, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.BER_ours.setFont(font)
        self.BER_ours.setStyleSheet("border-width: 0px;\n"
                                    "border-style: solid;\n"
                                    "")
        self.BER_ours.setReadOnly(True)
        self.BER_ours.setObjectName("BER_ours")
        self.selectInput_2 = QtWidgets.QPushButton(self.centralwidget)
        self.selectInput_2.setGeometry(QtCore.QRect(60, 640, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.selectInput_2.setFont(font)
        self.selectInput_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.selectInput_2.setMouseTracking(False)
        self.selectInput_2.setStyleSheet("\n"
                                         "border-style:solid;\n"
                                         "border-color: rgb(0, 0, 0);\n"
                                         "border-width: 5px;\n"
                                         "border-radius: 10px;\n"
                                         "background-color: rgb(150, 150, 150);")
        self.selectInput_2.setObjectName("selectInput_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(170, 690, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.saveOutput_2 = QtWidgets.QPushButton(self.centralwidget)
        self.saveOutput_2.setGeometry(QtCore.QRect(1280, 630, 101, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.saveOutput_2.setFont(font)
        self.saveOutput_2.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.saveOutput_2.setStyleSheet("\n"
                                        "border-style:solid;\n"
                                        "border-color: rgb(0, 0, 0);\n"
                                        "border-width: 5px;\n"
                                        "border-radius: 10px;\n"
                                        "background-color: rgb(150, 150, 150);")
        self.saveOutput_2.setAutoRepeatInterval(99)
        self.saveOutput_2.setAutoDefault(False)
        self.saveOutput_2.setDefault(False)
        self.saveOutput_2.setObjectName("saveOutput_2")
        self.selectInput_3 = QtWidgets.QPushButton(self.centralwidget)
        self.selectInput_3.setGeometry(QtCore.QRect(210, 640, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.selectInput_3.setFont(font)
        self.selectInput_3.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.selectInput_3.setMouseTracking(False)
        self.selectInput_3.setStyleSheet("\n"
                                         "border-style:solid;\n"
                                         "border-color: rgb(0, 0, 0);\n"
                                         "border-width: 5px;\n"
                                         "border-radius: 10px;\n"
                                         "background-color: rgb(150, 150, 150);")
        self.selectInput_3.setObjectName("selectInput_3")
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(1350, 240, 20, 331))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        self.line_5.setFont(font)
        self.line_5.setLineWidth(4)
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(1240, 240, 20, 331))
        self.line_6.setLineWidth(4)
        self.line_6.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.line_7 = QtWidgets.QFrame(self.centralwidget)
        self.line_7.setGeometry(QtCore.QRect(1170, 340, 311, 16))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(40, 40, 47))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.line_7.setPalette(palette)
        self.line_7.setLineWidth(4)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.line_8 = QtWidgets.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(1170, 420, 311, 16))
        self.line_8.setLineWidth(4)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.line_9 = QtWidgets.QFrame(self.centralwidget)
        self.line_9.setGeometry(QtCore.QRect(1170, 500, 311, 16))
        self.line_9.setLineWidth(4)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.line_10 = QtWidgets.QFrame(self.centralwidget)
        self.line_10.setGeometry(QtCore.QRect(1170, 270, 311, 16))
        self.line_10.setLineWidth(4)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.line_11 = QtWidgets.QFrame(self.centralwidget)
        self.line_11.setGeometry(QtCore.QRect(1170, 570, 311, 16))
        self.line_11.setLineWidth(4)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(1010, 100, 501, 51))
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.label_9.setFont(font)
        self.label_9.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.label_9.setStyleSheet("\n"
                                   "border-style:solid;\n"
                                   "border-color: rgb(0, 0, 0);\n"
                                   "border-width: 5px;\n"
                                   "border-radius: 5px;\n"
                                   "background-color: rgb(40, 40, 47);")
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1514, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setTitle("")
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "深度学习低光增强"))
        self.label_2.setText(_translate("MainWindow", "深度学习低光增强技术"))
        self.label_3.setText(_translate("MainWindow", "输入图像"))
        self.label_output.setText(_translate("MainWindow", "模型输出"))
        self.label_GT.setText(_translate("MainWindow", "真值"))
        self.selectInput.setText(_translate("MainWindow", "选择图像"))
        self.inputImagePath.setText(_translate("MainWindow", "输入图像路径: ..."))
        self.label_7.setText(_translate("MainWindow", "图片检测"))
        self.label_8.setText(_translate("MainWindow", "使用说明"))
        self.saveOutput.setText(_translate("MainWindow", "保存结果"))
        self.label_14.setText(_translate("MainWindow", "指标对比"))
        self.label_18.setText(_translate("MainWindow", "BRISQUE↓"))
        self.IoU_baseline.setText(_translate("MainWindow", "0.00"))
        self.PA_baseline.setText(_translate("MainWindow", "00.00"))
        self.label_19.setText(_translate("MainWindow", "NIQE↓"))
        self.label_20.setText(_translate("MainWindow", "PIQE↑"))
        self.MAE_baseline.setText(_translate("MainWindow", "00.00"))
        self.label_21.setText(_translate("MainWindow", "CEIQ↑"))
        self.PA_ours.setText(_translate("MainWindow", "00.00"))
        self.label_15.setText(_translate("MainWindow", "SCI"))
        self.label_16.setText(_translate("MainWindow", "Ours"))
        self.IoU_ours.setText(_translate("MainWindow", "0.00"))
        self.MAE_ours.setText(_translate("MainWindow", "00.00"))
        self.BER_baseline.setText(_translate("MainWindow", "00.00"))
        self.BER_ours.setText(_translate("MainWindow", "00.00"))
        self.selectInput_2.setText(_translate("MainWindow", "批量预测"))
        self.label_4.setText(_translate("MainWindow", "进度："))
        self.saveOutput_2.setText(_translate("MainWindow", "复制指标"))
        self.selectInput_3.setText(_translate("MainWindow", "退出系统"))
        self.label_9.setText(_translate("MainWindow", "关于团队"))


class Ui_platform(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
        self._img = None
        self._gt = None
        self._pred = None

        self.selectInput.clicked.connect(self.openImage)
        self.saveOutput.clicked.connect(self.saveImage)
        self.empty_metric = {'iou': 0., 'pa': 0., 'mae': 0., 'ber': 0.}

    def openFileNameDialog(self, title: str, exts: List[str]):
        exts_dict: Dict[str, str] = {
            ".jpg": "JPEG 图像文件 (*.jpg)",
            ".png": "PNG 图像文件 (*.png)",
        }
        exts = list(map(lambda x: exts_dict[x], exts))
        exts = ";;".join(exts)
        fileName, _ = QFileDialog.getOpenFileName(self, title, "", exts)
        return fileName

    def openDirectoryDialog(self, title: str):
        path = QFileDialog.getExistingDirectory(self, title, "")
        return path

    def saveImage(self):
        if self._pred == None:
            return
        dir = self.openDirectoryDialog("选择保存路径")
        self._pred.save(os.path.join(dir, "output.png"))

    def set_baseline_metrics(self, metric):
        _translate = QtCore.QCoreApplication.translate

        self.IoU_baseline.setText(_translate(
            "MainWindow", f"{metric['iou']:.3f}"))
        self.PA_baseline.setText(_translate(
            "MainWindow", f"{metric['pa']:.3f}"))
        self.MAE_baseline.setText(_translate(
            "MainWindow", f"{metric['mae']:.3f}"))
        self.BER_baseline.setText(_translate(
            "MainWindow", f"{metric['ber']:.3f}"))

    def set_model_metrics(self, metric):
        _translate = QtCore.QCoreApplication.translate

        self.IoU_ours.setText(_translate("MainWindow", f"{metric['iou']:.3f}"))
        self.PA_ours.setText(_translate("MainWindow", f"{metric['pa']:.3f}"))
        self.MAE_ours.setText(_translate("MainWindow", f"{metric['mae']:.3f}"))
        self.BER_ours.setText(_translate("MainWindow", f"{metric['ber']:.3f}"))

    def openImage(self):
        _translate = QtCore.QCoreApplication.translate

        img_path = self.openFileNameDialog("选择输入图像", [".jpg"])
        gt_path = img_path.split('.')[0] + "_gt." + img_path.split('.')[1]
        self.inputImagePath.setText(_translate(
            "MainWindow", f"输入图像路径: {img_path}"))
        id = os.path.basename(img_path).split('.')[0]
        self._img = Image.open(img_path)
        self._gt = Image.open(gt_path)
        self._pred = None
        self._img.save("./tmp/img.png")
        self._gt.save("./tmp/gt.png")
        self.progressBar.setValue(20)
        self.inputImage.setPixmap(QtGui.QPixmap(
            os.path.abspath("./tmp/img.png")))
        self.GT.setPixmap(QtGui.QPixmap(os.path.abspath("./tmp/gt.png")))
        self.outputImage.setPixmap(QtGui.QPixmap(
            os.path.abspath("placeholder.png")))
        self.progressBar.setValue(50)
        self._pred, pre_metric, baseline_metric = inference(
            id, self._img, self._gt, gdapi.metrics, gdapi.base_metrics)
        self.set_baseline_metrics(baseline_metric)
        self.set_model_metrics(pre_metric)
        self.progressBar.setValue(75)
        self._pred.save("./tmp/pred.png")
        self.outputImage.setPixmap(QtGui.QPixmap(
             os.path.abspath("./tmp/pred.png")))
        # self.set_baseline_metrics(baseline_metrics)
        # self.set_model_metrics(ours_metrics)
        self.progressBar.setValue(100)
