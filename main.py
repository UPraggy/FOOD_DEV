from PyQt5.QtWidgets import(QApplication, QMainWindow)
from PyQt5 import QtCore
from PyQt5.QtGui import QIcon
from utils.INTERFACE_FUNCIONALITIES.FOOD_DEV import Ui_MainWindow
from utils.INTERFACE_FUNCIONALITIES.Alert_win import Ui_Alert_win
from utils import interface_func as i_fun
from utils import template
import sys

p = template.Product()
c = template.Client()

i_fun = i_fun.Interface()
current_path = sys.path[0]

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
            #self.setWindowState(QtCore.Qt.WindowMinimized)

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
    
    def waiting_close_alert(self):
            self.alert.hide()
            self.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    p.view()
    c.view()
    i_fun.functionalties(w)
    w.show()
    sys.exit(app.exec_())
