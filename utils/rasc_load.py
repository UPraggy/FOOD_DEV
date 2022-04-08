from PyQt5.QtWidgets import(QApplication, QMainWindow, QWidget, QPushButton)
import utils
from utils.INTERFACE_FUNCIONALITIES.FOOD_DEV import Ui_MainWindow
from utils.INTERFACE_FUNCIONALITIES.LOADING import Ui_Form
from utils import interface_func as i_fun
from utils import template

p = template.Product()
c = template.Client()

i_fun = i_fun.Interface()
class AnotherWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.a = AnotherWindow()
        self.value = 0
    def show_window(self,w):
        self.a.pushButton.clicked.connect(lambda: self.toggle_window(w))
        self.a.frame_progress.setValue(self.value)
        self.a.show()
        w.toggle_window(w)
        sys.exit(app.exec_())
    def toggle_window(self, w):
        self.value += 10
        self.a.frame_progress.setValue(self.value)
        #if w.isVisible():
        #    w.hide()
        #else:
        #    w.show()

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show_window(w)
    p.view()
    c.view()
    i_fun.functionalties(w)
    sys.exit(app.exec_())

    


