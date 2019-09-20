from Project import butter


class Filter:  # 滤波器类
    normal_freq_cut = 0

    def __init__(self, freq_cut, freq):
        self.normal_freq_cut = 2 * freq_cut / freq  # 归一化截止频率

    def butter_low_pass(self, order=5):  # 返回一个低通滤波器
        return butter(order, self.normal_freq_cut, btype="lowpass")


# def butter_band(freqs, freq, order=5):  # 带通滤波，保留中间频率信号
#     normal_freq_cut = [get_normal_cut_fs(freqs[0], freq), get_normal_cut_fs(freqs[1], freq)]
#     return butter(order, normal_freq_cut, btype="bandpass")
