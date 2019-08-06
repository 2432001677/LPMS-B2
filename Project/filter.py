import numpy as np
from scipy.signal import butter, lfilter, filtfilt
import matplotlib.pyplot as plt


def get_normal_cut_fs(freq_cut, freq):  # 归一化截止频率
    return 2 * freq_cut / freq


def butter_low_pass(freq_cut, freq, order=5):
    normal_freq_cut = get_normal_cut_fs(freq_cut, freq)
    return butter(order, normal_freq_cut, btype="lowpass")


def butter_band(freqs, freq, order=5):
    normal_freq_cut = [get_normal_cut_fs(freqs[0], freq), get_normal_cut_fs(freqs[1], freq)]
    return butter(order, normal_freq_cut, btype="bandpass")


def show(order, freq_cut, fs):
    b, a = butter_low_pass(freq_cut, fs, order)
    # b, a = butter_band([10, 100], fs, order)
    data = np.loadtxt('./butterfly1.csv', delimiter=',', dtype=float, usecols=(6,), skiprows=1)
    # y = lfilter(b, a, data)  # 有偏移量
    y = filtfilt(b, a, data)
    plt.plot(data[20000:21000], 'b-', label='data')
    plt.plot(y[20000:21000], 'g-', linewidth=2, label='filtered data')
    plt.xlabel('Time [sec]')
    plt.title("order:" + str(order) + "  fs_cut:" + str(freq_cut))
    plt.grid()
    plt.legend()
    plt.subplots_adjust(hspace=0.35)
    plt.show()


def main():
    order = 6  # 滤波器阶数
    fs = 400.0  # 采样率 hz
    freq_cut = 15  # 截止频率
    show(order, freq_cut, fs)


if __name__ == '__main__':
    main()
