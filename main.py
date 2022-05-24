from PyQt5.QtWidgets import(QApplication, QMainWindow)
from PyQt5.QtGui import QIcon
from utils.INTERFACE_FUNCIONALITIES.FOOD_DEV import Ui_MainWindow, Ui_RMOR_slct_p_win, Ui_Alert_win
from utils import interface_func as i_fun
from sys import path as sys_path
from sys import exit as sys_exit
from sys import argv as sys_argv
from os import getcwd
from os.path import realpath 

i_fun = i_fun.Interface()

temp = 0
temp2 = 0
try:
    temp = sys_path[0]
    temp2 = temp.split(r'AppData')
except:
    current_path = temp
    
try:
    temp = getcwd() 
    temp2 = temp.split(r'AppData')
except:
    current_path = temp 

try:
    temp = realpath(__file__) 
    temp2 = temp.split(r'AppData')
except:
    current_path = temp 
    

class AlertWindow(QMainWindow, Ui_Alert_win):
    def __init__(self, parent=None):
        super(AlertWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(f'{current_path}/utils/INTERFACE_FUNCIONALITIES/Interface_files/LOGO.png'))
        self.setWindowTitle("ALERT - FOOD_DEV")
        self._want_to_close = False

    def closeEvent(self, evnt):
        if self._want_to_close:
            super(AlertWindow, self).closeEvent(evnt)
        else:
            evnt.ignore()

class Rmor_slct_p(QMainWindow, Ui_RMOR_slct_p_win):
    def __init__(self, parent=None):
        super(Rmor_slct_p, self).__init__(parent=parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon(f'{current_path}/utils/INTERFACE_FUNCIONALITIES/Interface_files/LOGO.png'))
        self.setWindowTitle("SELECT PRODUCT - FOOD_DEV")

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setupUi(self)
        self.show()
        self.setWindowIcon(QIcon(f'{current_path}/utils/INTERFACE_FUNCIONALITIES/Interface_files/LOGO.png'))
        self.setWindowTitle("FOOD_DEV")
        self.alert = AlertWindow()
        self.alert.hide()
        self.alert.Alert_win_f1_btn.clicked.connect(lambda: self.waiting_close_alert())
        self.rmor_slc_p = Rmor_slct_p()
    
    def waiting_close_alert(self):
            self.alert.hide()
            self.show()



if __name__ == "__main__":
    app = QApplication(sys_argv)
    w = MainWindow()
    i_fun.functionalties(w)
    w.show()
    sys_exit(app.exec_())







    
