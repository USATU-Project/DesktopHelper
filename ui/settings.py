# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'folderselect.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(514, 382)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("test.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("test.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.music_folder = QtWidgets.QTextEdit(self.centralwidget)
        self.music_folder.setMinimumSize(QtCore.QSize(330, 30))
        self.music_folder.setMaximumSize(QtCore.QSize(12235234, 27))
        self.music_folder.setObjectName("music_folder")
        self.horizontalLayout.addWidget(self.music_folder)
        self.music_button = QtWidgets.QPushButton(self.centralwidget)
        self.music_button.setObjectName("music_button")
        self.horizontalLayout.addWidget(self.music_button)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.video_folder = QtWidgets.QTextEdit(self.centralwidget)
        self.video_folder.setMinimumSize(QtCore.QSize(330, 30))
        self.video_folder.setMaximumSize(QtCore.QSize(124145, 30))
        self.video_folder.setObjectName("video_folder")
        self.horizontalLayout_2.addWidget(self.video_folder)
        self.video_button = QtWidgets.QPushButton(self.centralwidget)
        self.video_button.setObjectName("video_button")
        self.horizontalLayout_2.addWidget(self.video_button)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.photo_folder = QtWidgets.QTextEdit(self.centralwidget)
        self.photo_folder.setMinimumSize(QtCore.QSize(389, 27))
        self.photo_folder.setMaximumSize(QtCore.QSize(124142, 30))
        self.photo_folder.setObjectName("photo_folder")
        self.horizontalLayout_3.addWidget(self.photo_folder)
        self.photo_button = QtWidgets.QPushButton(self.centralwidget)
        self.photo_button.setObjectName("photo_button")
        self.horizontalLayout_3.addWidget(self.photo_button)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.other_folder = QtWidgets.QTextEdit(self.centralwidget)
        self.other_folder.setMinimumSize(QtCore.QSize(389, 27))
        self.other_folder.setMaximumSize(QtCore.QSize(25235, 30))
        self.other_folder.setObjectName("other_folder")
        self.horizontalLayout_4.addWidget(self.other_folder)
        self.other_button = QtWidgets.QPushButton(self.centralwidget)
        self.other_button.setObjectName("other_button")
        self.horizontalLayout_4.addWidget(self.other_button)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.accept_button = QtWidgets.QPushButton(self.centralwidget)
        self.accept_button.setObjectName("accept_button")
        self.horizontalLayout_5.addWidget(self.accept_button)
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_5.addWidget(self.cancel_button)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DesktopHelper[Settings]"))
        self.label.setText(_translate("MainWindow", "Настроить папку расположения"))
        self.label_2.setText(_translate("MainWindow", "Музыка"))
        self.music_button.setText(_translate("MainWindow", "Выбрать"))
        self.label_3.setText(_translate("MainWindow", "Видео"))
        self.video_button.setText(_translate("MainWindow", "Выбрать"))
        self.label_4.setText(_translate("MainWindow", "Фото"))
        self.photo_button.setText(_translate("MainWindow", "Выбрать"))
        self.label_5.setText(_translate("MainWindow", "Остальное"))
        self.other_button.setText(_translate("MainWindow", "Выбрать"))
        self.accept_button.setText(_translate("MainWindow", "Применить"))
        self.cancel_button.setText(_translate("MainWindow", "Отмена"))
