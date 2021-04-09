import sys
import os

from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication

from ui import folderselect, settings, logs

def_dir = os.getcwd()
dir_mus = def_dir+"/Music"
dir_vid = def_dir+"/Video"
dir_pho = def_dir+"/Photo"
dir_oth = def_dir+"/Other"

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

    def accept_but(self):
        self.set_dir()
        self.w3 = LogWindow()
        self.w3.show()
        self.close()

class Settings(QMainWindow, settings.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.music_folder.setText(dir_mus)
        self.photo_folder.setText(dir_pho)
        self.video_folder.setText(dir_vid)
        self.other_folder.setText(dir_oth)
        self.cancel_button.clicked.connect(self.close)
        self.accept_button.clicked.connect(self.accept_but)
    
    def accept_but(self):
        global dir_mus, dir_vid, dir_pho, dir_oth
        dir_mus = self.music_folder.toPlainText()
        dir_vid = self.video_folder.toPlainText()
        dir_pho = self.photo_folder.toPlainText()
        dir_oth = self.other_folder.toPlainText()
        self.close()

class LogWindow(QMainWindow, logs.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self) 

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
