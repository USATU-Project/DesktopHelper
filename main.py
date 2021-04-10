import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication

from ui import folderselect, settings, logs
from lib import files

def_dir = os.getcwd()
dir_mus = def_dir+"/Music"
dir_vid = def_dir+"/Video"
dir_pho = def_dir+"/Photo"
dir_oth = def_dir+"/Other"
set_dir = False

class MainApp(QMainWindow, folderselect.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.folder_select.setText(def_dir)
        self.settings_button.clicked.connect(self.settings_window)
        self.select_button.clicked.connect(self.fold_sel)
        self.accept_button.clicked.connect(self.accept_but)
        self.cancel_button.clicked.connect(QCoreApplication.instance().quit)

    def settings_window(self):
        self.set_dir()
        self.w2 = Settings()
        self.w2.show()
        
    def fold_sel(self):
        directory = QFileDialog.getExistingDirectory(self, "Выберите папку...")
        if (directory != ""):
            self.folder_select.setText(directory)
    
    def set_dir(self):
        global def_dir
        directory = self.folder_select.toPlainText()
        def_dir = directory

    def make_fol(self, path):
        if not os.path.isdir(path):
            os.mkdir(path)

    def accept_but(self):
        self.set_dir()
        if not set_dir:
            global dir_mus, dir_oth, dir_pho, dir_vid
            dir_mus = def_dir+"/Music"
            dir_oth = def_dir+"/Other"
            dir_pho = def_dir+"/Photo"
            dir_vid = def_dir+"/Video"
            
        for i in [dir_mus, dir_oth, dir_pho, dir_vid, dir_oth+"/Arc", dir_oth+"/App", dir_oth+"/Doc"]:
            self.make_fol(i)
        self.w3 = LogWindow()
        self.w3.show()
        self.close()

class Settings(QMainWindow, settings.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.music_folder.setText(def_dir+"/Music")
        self.photo_folder.setText(def_dir+"/Photo")
        self.video_folder.setText(def_dir+"/Video")
        self.other_folder.setText(def_dir+"/Other")
        self.cancel_button.clicked.connect(self.close)
        self.accept_button.clicked.connect(self.accept_but)
    
    def accept_but(self):
        global dir_mus, dir_vid, dir_pho, dir_oth, set_dir
        dir_mus = self.music_folder.toPlainText()
        dir_vid = self.video_folder.toPlainText()
        dir_pho = self.photo_folder.toPlainText()
        dir_oth = self.other_folder.toPlainText()
        set_dir = True
        self.close()

class LogWindow(QMainWindow, logs.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Sort()
        self.cancel_button.clicked.connect(QCoreApplication.instance().quit)
    def Sort(self):
        list_file = os.listdir(def_dir)
        for i in list_file:
            tmp = i.split('.')
            if os.path.isdir(def_dir+"/"+i):
                if def_dir+"/"+i != dir_pho and def_dir+"/"+i != dir_vid and def_dir+"/"+i != dir_mus and def_dir+"/"+i != dir_oth:
                    os.replace(def_dir+"/"+i,dir_oth+"/"+i)
                    self.logs_list.addItem(dir_oth+"/"+i)
                continue
            for j in files.Files:
                for k in j.value:
                    if (tmp[1] == k):
                        if (j.name == "pho"):
                            os.replace(def_dir+"/"+i,dir_pho+"/"+i)
                            self.logs_list.addItem(dir_pho+"/"+i)
                            break
                        elif (j.name == "vid"):
                            os.replace(def_dir+"/"+i,dir_vid+"/"+i)
                            self.logs_list.addItem(dir_vid+"/"+i)
                            break
                        elif (j.name == "mus"):
                            os.replace(def_dir+"/"+i,dir_mus+"/"+i)
                            self.logs_list.addItem(dir_mus+"/"+i)
                            break
                        elif (j.name == "doc"):
                            os.replace(def_dir+"/"+i,dir_oth+"/Doc/"+i)
                            self.logs_list.addItem(dir_oth+"/Doc/"+i)
                            break
                        elif (j.name == "arc"):
                            os.replace(def_dir+"/"+i,dir_oth+"/Arc/"+i)
                            self.logs_list.addItem(dir_oth+"/Arc/"+i)
                            break
                        else
                            os.replace(def_dir+"/"+i,dir_oth+"/App/"+i)
                            self.logs_list.addItem(dir_oth+"/App/"+i)
                            break

                if os.path.isfile(def_dir+"/"+i):
                    os.replace(def_dir+"/"+i,dir_oth+"/"+i)
                    self.logs_list.addItem(dir_oth+"/"+i)
def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
