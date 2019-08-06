from project import butter


def get_normal_cut_fs(freq_cut, freq):  # 归一化截止频率
    return 2 * freq_cut / freq


def butter_low_pass(freq_cut, freq, order=5):
    normal_freq_cut = get_normal_cut_fs(freq_cut, freq)
    return butter(order, normal_freq_cut, btype="lowpass")


def butter_band(freqs, freq, order=5):
    normal_freq_cut = [get_normal_cut_fs(freqs[0], freq), get_normal_cut_fs(freqs[1], freq)]
    return butter(order, normal_freq_cut, btype="bandpass")


