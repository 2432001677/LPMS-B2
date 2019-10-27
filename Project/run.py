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
    filter = Filter(freq_cut, fs) # 新建一个滤波器
    b, a = filter.butter_low_pass(order)  # 生成一个分子b,分母a的低通滤波器
    # b, a = butter_band([10, 100], fs, order)

    file = "freestyle1.csv"
    data = Data(file)  # 读文件
    data_x = data.get_gyro()[0]
    data_y = data.get_gyro()[1]
    data_z = data.get_gyro()[2]
    # y = lfilter(b, a, data)  # 有偏移量
    y = [filtfilt(b, a, data_x), filtfilt(b, a, data_y), filtfilt(b, a, data_z)]  # 无偏移量的处理后的数据列表

    #generate_images(y, freq_cut, order,file)
    # data_sta(y)

    # butterfly=Swim()
    # butterfly.gyro=y
    # print(np.min(y[0][23700:23900]),end=' ')
    # print(np.argmin(y[0][23700:23900])+23700)
    # print(np.max(y[1][23700:23900]),end=' ')
    # print(np.argmax(y[1][23700:23900])+23700)
    # print(np.max(y[2][23700:23900]),end=' ')
    # print(np.argmax(y[2][23700:23900])+23700)
    start_time=0
    end_time=len(y[2])
    #limit=(-1500,2000)
    plt.subplot(311)
    plt.plot(y[0][start_time:end_time])
    #plt.ylim(limit)
    plt.grid()
    plt.title("freestyle1")
    plt.subplot(312)
    plt.plot(y[1][start_time:end_time])
    #plt.ylim(limit)
    plt.grid()
    plt.subplot(313)
    plt.plot(y[2][start_time:end_time])
    #plt.ylim(limit)
    plt.grid()

    # plt.savefig("../1", dpi=1000)
    plt.show()
    s = Swim()
    #     flg = 5000
    # free=0
    # butter=0
    # back=0
    # breast=0
    # while start_time <= end_time-flg:
    #     s.time_point_list.clear()
    #     s.get_frequency(y[2], start_time, start_time+flg)
    #     name = s.tst()
    #     if name == "freestyle":
    #         free += 1
    #     if name == "butterfly":
    #         butter += 1
    #     if name == "backstroke":
    #         back += 1
    #     if name == "breaststroke":
    #         breast += 1
    #     start_time+=flg
    # if free>butter and free>butter and free>breast:
    #     s.name="freestyle"
    #     s.time_frame_interval = 500  # 时间帧覆盖窗口大小
    #     s.flag = 1000
    #     s.flag2 = 500
    #
    #     list_z =s.get_frequency(y[2], start_time, end_time)
    # if butter > free and butter > breast and butter > back:
    #     s.name = "butterfly"
    #     s.time_frame_interval = 500  # 时间帧覆盖窗口大小
    #     s.flag = 1000
    #     s.flag2 = 500
    #
    #     list_z =s.get_frequency(y[2], start_time, end_time)
    # if back > butter and back > free and back > breast:
    #     s.name = "backstroke"
    #     s.time_frame_interval = 600  # 时间帧覆盖窗口大小
    #     s.flag = 700
    #     s.flag2 = 400
    #
    #     list_z =s.get_frequency(y[2], start_time, end_time)
    # if breast > butter and breast > free and breast > back:
    #     s.name = "breaststroke"
    #     s.time_frame_interval = 600  # 时间帧覆盖窗口大小
    #     s.flag = 400
    #     s.flag2 = 300
    #
    #     list_z=s.get_frequency(y[2], start_time, end_time)
    list_z=s.get_frequency( )
    print(s.tst())
    s.print_inf()
    # print(free,butter,back,breast)
    print(list_z)
    # print(np.ptp(y[2][26000:34000]))
    # print(np.amax(y[2][26000:34000]))
    # for i in list_z:
    #     print(y[2][i])

if __name__ == '__main__':
    main()
