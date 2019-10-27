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
        self.summary_time.setDisplayFormat("HH:mm:ss")

        self.refresh_list_swim_view()
        self.refresh_frame_sum()

        self.listView_swims.clicked.connect(self.refresh)
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

    def refresh(self):
        self.refresh_frame_sum()
        self.refresh_table_view()

    def refresh_table_view(self):
        pass

    def refresh_frame_sum(self):
        pos = self.listView_swims.currentIndex()
        self.text_main_swim.setText(self.controller.swim_list[pos.row()].name)
        hour = self.controller.swim_list[pos.row()].all_time // 1000 // 60 // 60
        minute = self.controller.swim_list[pos.row()].all_time // 1000 // 60 % 60
        sec = self.controller.swim_list[pos.row()].all_time // 1000 % 60
        self.summary_time.setTime(QtCore.QTime(hour, minute, sec))
        self.label_calorie_num.setText(str(round(self.controller.swim_list[pos.row()].all_time / 1000 * 0.8, 2)) + "千卡")
        try:
            self.label_average_speed_num.setText(str(round(self.controller.swim_list[pos.row()].all_time / (
                    self.controller.swim_list[pos.row()].number * self.controller.swim_list[pos.row()].arm_stroke), 2)))
        except Exception:
            self.label_average_speed_num.setText("NAN")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())
