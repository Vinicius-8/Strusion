import os
import sys
import inspect
from PyQt5 import QtWidgets
sys.path.append('..')

absolute_path = os.path.abspath(inspect.getfile(inspect.currentframe()))
current_dir = os.path.dirname(absolute_path)
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from Strusion.gui import strusion_gui as gui


def test_variables():
    app = QtWidgets.QApplication(sys.argv)
 
    MainWindow = QtWidgets.QMainWindow()
    ui = gui.Ui_MainWindow()
    ui.setupUi(MainWindow)

    ui.label
    ui.label_path
    ui.button_load
    ui.spinBox
    ui.button_run
    ui.actionOpen
  

    
    #ui = Ui_MainWindow()
    #ui.setupUi(MainWindow)
    #MainWindow.show()
    #sys.exit(app.exec_())
