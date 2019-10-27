import os

from scipy.signal import filtfilt

from Project.filter import Filter
from Project.WinUI.readfile import Data
from Project.swim import Swim


class Files:
    def __init__(self):
        self.swim_list = []
        self.swim_file_list = []

        start_time = 0
        order = 6  # 滤波器阶数
        fs = 400.0  # 采样率 hz
        freq_cut = 15  # 截止频率
        filter = Filter(freq_cut, fs)  # 新建一个滤波器
        b, a = filter.butter_low_pass(order)  # 生成一个分子b,分母a的低通滤波器

        path = os.getcwd() + "/../../data/"
        for dirpath, dirnames, filenames in os.walk(path):
            for i in filenames:
                print(i)
                data = Data(i)  # 读文件
                data_x = data.get_gyro()[0]
                data_y = data.get_gyro()[1]
                data_z = data.get_gyro()[2]
                end_time = len(data_z)
                y = [filtfilt(b, a, data_x), filtfilt(b, a, data_y), filtfilt(b, a, data_z)]  # 无偏移量的处理后的数据列表
                self.swim_list.append(Swim(y[2], start_time, end_time))
                self.swim_file_list.append(i)


if __name__ == '__main__':
    f = Files()
