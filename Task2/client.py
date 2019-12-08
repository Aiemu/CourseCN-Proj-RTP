import sys

from ui import Ui_MainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets

class Pages:
    def __init__(self):
        self.page_main = Ui_MainWindow()

pages = Pages()
app = QtWidgets.QApplication(sys.argv)
page_main = QtWidgets.QMainWindow()
pages.page_main.setupUi(page_main)
page_main.show()
sys.exit(app.exec_())