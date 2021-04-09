import sys
import os

from PyQt5 import QtWidgets

from ui import folderselect
from ui import settings

def_dir = os.getcwd()


class MainApp(QtWidgets.QMainWindow, folderselect.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings_button.clicked.connect(self.settings_window)
        self.select_button.clicked.connect(self.fold_sel)

    def settings_window(self):
        self.w2 = Settings()
        self.w2.show()
        
    def fold_sel(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(self, "Выберите папку...")
        global def_dir
        def_dir = directory
        self.folder_select.setText(directory)

class Settings(QtWidgets.QMainWindow, settings.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == '__main__':
    main()
