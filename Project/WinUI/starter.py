import sys

from PyQt5 import QtWidgets
from scipy.signal import filtfilt

from Project.WinUI.WindowUI import Ui_MainWindow

from PyQt5.QtWidgets import QMainWindow, QApplication

from Project.filter import Filter
from Project.readfile import Data
from Project.swim import Swim


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.bt_quit.clicked.connect(QtWidgets.qApp.quit)
        self.bt_summary.clicked.connect(self.change_to_summary)
        self.bt_detail.clicked.connect(self.change_to_detail)




    def retranslateUi(self, MainWindow):
        Ui_MainWindow.retranslateUi(self, MainWindow)
        self.frame_detail.close()

    def change_to_summary(self):
        self.frame_detail.close()
        self.frame_sum.show()

    def change_to_detail(self):
        self.frame_sum.close()
        self.frame_detail.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
