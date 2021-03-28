from PyQt5 import QtWidgets, QtCore
from strusion_gui import Ui_MainWindow
import os
import sys
import inspect

sys.path.append('..')
absolute_path = os.path.abspath(inspect.getfile(inspect.currentframe()))
current_dir = os.path.dirname(absolute_path)
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

import subtitles
import IO
# from Strusion import subtitles


class SyncImplementation(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self, mainWindow):
       super(SyncImplementation, self).__init__()
       mainWindow.setFixedSize(self.size().width()+60, self.size().height()-120) # fixing size
       # mainWindow.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)
       self.setupUi(mainWindow)
       self.label_path.setText('...')
       self.actionOpen.triggered.connect(lambda: self.__click_load_file())
       self.button_load.clicked.connect(lambda: self.__click_load_file())
       self.button_run.clicked.connect(self.__save_synced_subtitle)


       self.original_sub = ''

    def __click_load_file(self):
        self.original_sub = self.__explore_files()
        splited = self.original_sub.split('/')
        self.label_path.setText(splited[-1] if len(splited)>1 else self.original_sub)
        # self.label_path.setStatusTip(self.original_sub)
        self.label_path.setToolTip(self.original_sub)


    def __explore_files(self):
        # explore folders to select a file
        file_path = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File','c:\\', "Subtitle (*.srt)")
        return file_path[0]


    def __explore_path(self, path):
        # explore folders to select a path
        path = QtWidgets.QFileDialog.getSaveFileName(self, 'Save file', path, "Subtitle (*.srt)")
        return path[0]

    def __save_synced_subtitle(self):
        delay = self.spinBox.value()
        try:
            if not self.original_sub:
                raise Exception('No file loaded')
            elif delay == 0:
                raise Exception('Delay can\'t be 0')
        except Exception as e:
            # print('Warning: '+ str(e))
            self.__message_box(e, 0)
            return

        # save path
        save_path = self.__explore_path(self.original_sub)

        # logic for sync
        changed_sub = subtitles.change_subtitle_delay(delay, self.original_sub)
        IO.output_file(save_path, changed_sub)
        self.__message_box('The file was saved', 1)

    def __message_box(self, message, type):
        icon = [QtWidgets.QMessageBox().Warning,
                QtWidgets.QMessageBox().Information,
                QtWidgets.QMessageBox().Critical,
                QtWidgets.QMessageBox().Question]


        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle('Warning')
        msg_box.setIcon(icon[type])
        msg_box.setText(str(message)+ '                                     ' )
        msg_box.exec_()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = SyncImplementation(MainWindow)
    # ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())




