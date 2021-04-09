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
        MainWindow.resize(530, 400)
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
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
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
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
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
        self.video_folder_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.video_folder_2.setMinimumSize(QtCore.QSize(389, 27))
        self.video_folder_2.setMaximumSize(QtCore.QSize(124142, 30))
        self.video_folder_2.setObjectName("video_folder_2")
        self.horizontalLayout_3.addWidget(self.video_folder_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
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
        self.video_folder_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.video_folder_3.setMinimumSize(QtCore.QSize(389, 27))
        self.video_folder_3.setMaximumSize(QtCore.QSize(25235, 30))
        self.video_folder_3.setObjectName("video_folder_3")
        self.horizontalLayout_4.addWidget(self.video_folder_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_4.addWidget(self.pushButton_4)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.date_sort = QtWidgets.QCheckBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        self.date_sort.setFont(font)
        self.date_sort.setObjectName("date_sort")
        self.verticalLayout.addWidget(self.date_sort)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.cancel_button = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_button.setObjectName("cancel_button")
        self.horizontalLayout_5.addWidget(self.cancel_button)
        self.accept_button = QtWidgets.QPushButton(self.centralwidget)
        self.accept_button.setObjectName("accept_button")
        self.horizontalLayout_5.addWidget(self.accept_button)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Настроить папку расположения"))
        self.label_2.setText(_translate("MainWindow", "Музыка"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.label_3.setText(_translate("MainWindow", "Видео"))
        self.pushButton_2.setText(_translate("MainWindow", "PushButton"))
        self.label_4.setText(_translate("MainWindow", "Фото"))
        self.pushButton_3.setText(_translate("MainWindow", "PushButton"))
        self.label_5.setText(_translate("MainWindow", "Остальное"))
        self.pushButton_4.setText(_translate("MainWindow", "PushButton"))
        self.date_sort.setText(_translate("MainWindow", "Сортировка по дате"))
        self.cancel_button.setText(_translate("MainWindow", "Отмена"))
        self.accept_button.setText(_translate("MainWindow", "Применить"))
