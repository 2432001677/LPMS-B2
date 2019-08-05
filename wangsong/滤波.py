import numpy as np
from scipy.signal import butter, lfilter, freqz
import matplotlib.pyplot as plt
import pandas as pd


def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a


def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y


order = 6
fs = 80.0  # 采样率 hz
cutoff = 3.667
b, a = butter_lowpass(cutoff, fs, order)
w, h = freqz(b, a, worN=800)
plt.subplot(2, 1, 1)
plt.plot(0.5*fs*w/np.pi, np.abs(h), 'b')
plt.plot(cutoff,0.5*np.sqrt(2), 'ko')
plt.axvline(cutoff, color='k')
plt.xlim(0, 0.5*fs)
plt.title("Lowpass Filter Frequency Response")
plt.xlabel('Frequency [HZ]')
plt.grid()
T = 5.0
n = int(T * fs)
t = np.linspace(0, T, n, endpoint=False)
#data = np.sin(1.2*2*np.pi*t) + 1.5*np.cos(9*2*np.pi*t) + 0.5*np.sin(12.0*2*np.pi*t)
data = np.loadtxt('./butterfly1.csv', delimiter=',', dtype=float,  usecols=(6,), skiprows=1)
y = butter_lowpass_filter(data, cutoff, fs, order)
plt.subplot(2, 1, 2)
plt.plot(data[20000:21000], 'b-', label='data')
plt.plot(y[20000:21000], 'g-', linewidth=2, label='filtered data')
plt.xlabel('Time [sec]')
plt.grid()
plt.legend()
plt.subplots_adjust(hspace=0.35)
plt.show()
