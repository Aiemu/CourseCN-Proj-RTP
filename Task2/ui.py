# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(24, 0, 751, 551))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_display = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_display.setText("")
        self.label_display.setObjectName("label_display")
        self.verticalLayout.addWidget(self.label_display)
        self.label_subtitle = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_subtitle.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_subtitle.setText("")
        self.label_subtitle.setObjectName("label_subtitle")
        self.verticalLayout.addWidget(self.label_subtitle)
        self.scrollLine = QtWidgets.QSlider(self.horizontalLayoutWidget_2)
        self.scrollLine.setOrientation(QtCore.Qt.Horizontal)
        self.scrollLine.setObjectName("scrollLine")
        self.verticalLayout.addWidget(self.scrollLine)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_setup = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_setup.setObjectName("btn_setup")
        self.horizontalLayout.addWidget(self.btn_setup)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_play = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_play.setObjectName("btn_play")
        self.horizontalLayout.addWidget(self.btn_play)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_pause = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_pause.setObjectName("btn_pause")
        self.horizontalLayout.addWidget(self.btn_pause)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_teardown = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.btn_teardown.setObjectName("btn_teardown")
        self.horizontalLayout.addWidget(self.btn_teardown)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.pushButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout.setStretch(0, 7)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 7)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 7)
        self.horizontalLayout.setStretch(5, 1)
        self.horizontalLayout.setStretch(6, 7)
        self.horizontalLayout.setStretch(7, 1)
        self.horizontalLayout.setStretch(8, 7)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout.setStretch(0, 40)
        self.verticalLayout.setStretch(3, 2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget_2)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_3.addWidget(self.listWidget)
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_5.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_5.addWidget(self.pushButton_3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.horizontalLayout_3.setStretch(0, 100)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 34)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_setup.setText(_translate("MainWindow", "Setup"))
        self.btn_play.setText(_translate("MainWindow", "Play"))
        self.btn_pause.setText(_translate("MainWindow", "Pause"))
        self.btn_teardown.setText(_translate("MainWindow", "Teardown"))
        self.pushButton.setText(_translate("MainWindow", "Fullscreen"))
        self.label.setText(_translate("MainWindow", "搜索"))
        self.label_2.setText(_translate("MainWindow", "视频列表"))
        self.label_3.setText(_translate("MainWindow", "音轨调整"))
        self.pushButton_2.setText(_translate("MainWindow", "-0.1s"))
        self.pushButton_3.setText(_translate("MainWindow", "+0.1s"))
