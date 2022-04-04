from PyQt5.QtWidgets import(QApplication, QMainWindow, QWidget)
import utils
from utils.INTERFACE_FUNCIONALITIES.FOOD_DEV import Ui_MainWindow
from utils import interface_func as i_fun

i_fun = i_fun.Interface()

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    i_fun.functionalties(w)
    w.show()
    sys.exit(app.exec_())

    


