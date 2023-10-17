# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BiliDownloader.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.showInfoButton = QtWidgets.QPushButton(self.centralwidget)
        self.showInfoButton.setObjectName("showInfoButton")
        self.horizontalLayout_3.addWidget(self.showInfoButton)
        self.downloadButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadButton.setEnabled(False)
        self.downloadButton.setObjectName("downloadButton")
        self.horizontalLayout_3.addWidget(self.downloadButton)
        self.downloadSaveAsButton = QtWidgets.QPushButton(self.centralwidget)
        self.downloadSaveAsButton.setEnabled(False)
        self.downloadSaveAsButton.setObjectName("downloadSaveAsButton")
        self.horizontalLayout_3.addWidget(self.downloadSaveAsButton)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 2)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.BVAV_Label = QtWidgets.QLabel(self.centralwidget)
        self.BVAV_Label.setObjectName("BVAV_Label")
        self.horizontalLayout.addWidget(self.BVAV_Label)
        self.BVAVInput = QtWidgets.QLineEdit(self.centralwidget)
        self.BVAVInput.setObjectName("BVAVInput")
        self.horizontalLayout.addWidget(self.BVAVInput)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.VideoInfoBox = QtWidgets.QTextBrowser(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.VideoInfoBox.setFont(font)
        self.VideoInfoBox.setObjectName("VideoInfoBox")
        self.gridLayout.addWidget(self.VideoInfoBox, 0, 1, 1, 1)
        self.logBox = QtWidgets.QTextBrowser(self.centralwidget)
        self.logBox.setObjectName("logBox")
        self.gridLayout.addWidget(self.logBox, 0, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 5, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menu_A = QtWidgets.QMenu(self.menubar)
        self.menu_A.setObjectName("menu_A")
        MainWindow.setMenuBar(self.menubar)
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menu_A.addAction(self.actionAbout)
        self.menubar.addAction(self.menu_A.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BiliDownloader"))
        self.showInfoButton.setText(_translate("MainWindow", "获取并显示视频信息"))
        self.downloadButton.setText(_translate("MainWindow", "下载"))
        self.downloadSaveAsButton.setText(_translate("MainWindow", "下载并另存为..."))
        self.label_2.setText(_translate("MainWindow", "日志"))
        self.label.setText(_translate("MainWindow", "视频信息"))
        self.BVAV_Label.setText(_translate("MainWindow", "BV/av号:"))
        self.menu_A.setTitle(_translate("MainWindow", "帮助(&H)"))
        self.actionAbout.setText(_translate("MainWindow", "关于..."))
import BiliDownloader_rc
