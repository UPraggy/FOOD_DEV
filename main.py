from PyQt5.QtWidgets import(QApplication, QMainWindow, QWidget, QLabel)
import utils
from utils.INTERFACE_FUNCIONALITIES.FOOD_DEV import Ui_MainWindow
from utils import interface_func as i_fun
from utils import template

p = template.Product()
c = template.Client()

i_fun = i_fun.Interface()

    
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.show()
        self.setMouseTracking(True)
        
    def mouseMoveEvent(self, event): 
        self.rmm_lb_logo.setStyleSheet("background-color: red;") #<-- TRY COLOR 
        #self.rmm_lb_logo.setText('Mouse coords: ( %d : %d )' % (event.x(), event.y()))


import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    p.view()
    c.view()
    i_fun.functionalties(w)
    w.show()
    sys.exit(app.exec_())
