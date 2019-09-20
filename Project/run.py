<<<<<<< HEAD
from Project.filter import Filter
from Project.show_plot import show
from Project import lfilter, filtfilt, np
from Project.statistics import data_sta
from Project.readfile import Data
=======
from Project.filter import butter_low_pass
from Project.show_plot import show
from Project import filtfilt, np
from Project.statistics import data_sta
>>>>>>> bc0d85cb0af4d9a1c9e7650809a78683ce0ac8e7


def main():
    order = 6  # 滤波器阶数
    fs = 400.0  # 采样率 hz
    freq_cut = 15  # 截止频率
<<<<<<< HEAD
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
=======
    b, a = butter_low_pass(freq_cut, fs, order)  # 滤波器构造函数 生成一个低通滤波器,分子b,分母a
    # b, a = butter_band([10, 100], fs, order)
    pwd = "../data/"
    file = "butterfly1.csv"
    data_x = np.loadtxt(pwd + file, delimiter=',', usecols=(6,), skiprows=1)  # 读文件
    data_y = np.loadtxt(pwd + file, delimiter=',', usecols=(7,), skiprows=1)
    data_z = np.loadtxt(pwd + file, delimiter=',', usecols=(8,), skiprows=1)
    # data = [data_x, data_y, data_z]
    # y = lfilter(b, a, data)  # 有偏移量
    y = [filtfilt(b, a, data_x), filtfilt(b, a, data_y), filtfilt(b, a, data_z)]  # 无偏移量
    show(y, freq_cut, order)
    data_sta(y)

if __name__ == '__main__':
    main()

>>>>>>> bc0d85cb0af4d9a1c9e7650809a78683ce0ac8e7
