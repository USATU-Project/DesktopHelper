import sys
import os

from PyQt5 import QtWidgets

import design

class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    dir1 = os.getcwd()
    dir2 = os.getcwd()
    def __init__(self):
        super().__init__()
        self.setupUi(self) 
        self.pushButton.clicked.connect(self.browse_folder1)
        self.pushButton_2.clicked.connect(self.browse_folder2) 
        self.pushButton_3.clicked.connect(self.accept) 

    def browse_folder1(self):
        directory1 = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")

        if directory1:
            self.listWidget.clear()
            self.dir1 = directory1
            self.listWidget.addItem("Текущая директория: "+directory1)

    def browse_folder2(self):
        directory2 = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку")

        if directory2:
            self.listWidget_2.clear()
            self.dir2 = directory2
            self.listWidget_2.addItem("Текущая директория: "+directory2)

    def accept(self):
        lst = os.listdir(self.dir1)
        for i in lst:
            a = i.split('.')
            if len(a) < 2:
                continue
            if a[1] == "jpg" and not os.path.exists(self.dir2+"/Picters"):
                os.mkdir(self.dir2+"/Picters")
            elif a[1] == "webm" and not os.path.exists(self.dir2+"/Video"):
                os.mkdir(self.dir2+"/Video")

        for i in lst:
            if len(a) < 2:
                continue
            if a[1] == "jpg":
                os.replace(self.dir1+"/"+i,self.dir2+"/Picters/"+i)
            elif a[1] == "webm":
                os.replace(self.dir1+"/"+i,self.dir2+"/Video/"+i)         

          

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
