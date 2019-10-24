import sys

from Project.WinUI.Controller import Files
from Project.WinUI.WindowUI import Ui_MainWindow
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtWidgets, QtCore


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.controller = Files()

        self.refresh_list_swim_view()

        self.listView_swims.clicked.connect(self.select_list_item)
        self.bt_summary.clicked.connect(self.change_to_summary)
        self.bt_detail.clicked.connect(self.change_to_detail)
        self.bt_quit.clicked.connect(QtWidgets.qApp.quit)

    def retranslateUi(self, MainWindow):
        Ui_MainWindow.retranslateUi(self, MainWindow)
        self.tableView_detail.close()

    def refresh_list_swim_view(self):
        list_model = QtCore.QStringListModel(self.controller.swim_file_list)
        self.listView_swims.setModel(list_model)

    def change_to_summary(self):
        self.tableView_detail.close()
        self.frame_sum.show()

    def change_to_detail(self):
        self.frame_sum.close()
        self.tableView_detail.show()

    def select_list_item(self):
        self.refresh_frame_sum()
        pass

    def refresh_frame_sum(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
