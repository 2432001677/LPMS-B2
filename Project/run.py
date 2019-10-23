from Project.filter import Filter
from Project.generate_images import generate_images
from Project import lfilter, filtfilt, np
from Project.statistics import data_sta
from Project.readfile import Data
from Project.swim import Swim
from Project import plt


def main():
    order = 6  # 滤波器阶数
    fs = 400.0  # 采样率 hz
    freq_cut = 15  # 截止频率
    filter = Filter(freq_cut, fs)  # 新建一个滤波器
    b, a = filter.butter_low_pass(order)  # 生成一个分子b,分母a的低通滤波器
    # b, a = butter_band([10, 100], fs, order)

    file = "butterfly1.csv"
    data = Data(file)  # 读文件
    data_x = data.get_gyro()[0]
    data_y = data.get_gyro()[1]
    data_z = data.get_gyro()[2]
    # y = lfilter(b, a, data)  # 有偏移量
    y = [filtfilt(b, a, data_x), filtfilt(b, a, data_y), filtfilt(b, a, data_z)]  # 无偏移量的处理后的数据列表

    # generate_images(y, freq_cut, order,file)
    # data_sta(y)

    # butterfly=Swim()
    # butterfly.gyro=y

    start_time = 30000
    end_time = 40000
    # print(np.min(y[0][start_time:end_time]), end=' ')
    # print(np.argmin(y[0][start:end_add]))
    # print(np.max(y[1][start:end_add]), end=' ')
    # print(np.argmax(y[1][start:end_add]))
    # print(np.max(y[2][start:end_add]), end=' ')
    # print(np.argmax(y[2][start:end_add]))

    limit = (-1500, 2000)
    plt.subplot(311)
    plt.plot(y[0][start_time:end_time])
    plt.ylim(limit)
    plt.grid()
    plt.subplot(312)
    plt.plot(y[1][start_time:end_time])
    plt.ylim(limit)
    plt.grid()
    plt.subplot(313)
    plt.plot(y[2][start_time:end_time])
    plt.ylim(limit)
    plt.grid()
    plt.show()
    s = Swim()

    list_z = s.get_frequency(y[2], start_time, end_time)
    print(list_z)


if __name__ == '__main__':
    main()
