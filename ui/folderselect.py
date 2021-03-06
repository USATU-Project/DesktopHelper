# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(538, 234)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("test.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.folder_select = QtWidgets.QTextEdit(self.centralwidget)
        self.folder_select.setMinimumSize(QtCore.QSize(330, 30))
        self.folder_select.setMaximumSize(QtCore.QSize(16777215, 30))
        self.folder_select.setObjectName("folder_select")
        self.horizontalLayout.addWidget(self.folder_select)
        self.select_button = QtWidgets.QPushButton(self.centralwidget)
        self.select_button.setMinimumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.select_button.setFont(font)
        self.select_button.setObjectName("select_button")
        self.horizontalLayout.addWidget(self.select_button)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.settings_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.settings_button.setFont(font)
        self.settings_button.setObjectName("settings_button")
        self.horizontalLayout_3.addWidget(self.settings_button)
        spacerItem = QtWidgets.QSpacerItem(378, 30, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.accept_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.accept_button.setFont(font)
        self.accept_button.setObjectName("accept_button")
        self.horizontalLayout_2.addWidget(self.accept_button)
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.cancel_button.setFont(font)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_2.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DesktopHelper"))
        self.select_button.setText(_translate("MainWindow", "??????????????"))
        self.settings_button.setText(_translate("MainWindow", "??????????????????"))
        self.accept_button.setText(_translate("MainWindow", "??????????????????"))
        self.cancel_button.setText(_translate("MainWindow", "????????????"))
