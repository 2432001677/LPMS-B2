from Project.filter import Filter
from Project.show_plot import show
from Project import lfilter, filtfilt, np
from Project.statistics import data_sta
from Project.readfile import Data


def main():
    order = 6  # 滤波器阶数
    fs = 400.0  # 采样率 hz
    freq_cut = 15  # 截止频率
    filter = Filter(freq_cut, fs) # 新建一个滤波器
    b, a = filter.butter_low_pass(order)  # 生成一个分子b,分母a的低通滤波器
    # b, a = butter_band([10, 100], fs, order)

    file = "butterfly1.csv"
    data = Data(file)  # 读文件
    data_x = data.get_gyro()[0]
    data_y = data.get_gyro()[1]
    data_z = data.get_gyro()[2]
    # y = lfilter(b, a, data)  # 有偏移量
    y = [filtfilt(b, a, data_x), filtfilt(b, a, data_y), filtfilt(b, a, data_z)]  # 无偏移量的处理后的数据列表

    show(y, freq_cut, order)
    data_sta(y)


if __name__ == '__main__':
    main()
