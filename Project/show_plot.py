from . import plt

import sys

def show(y, freq_cut, order):
    start = i = 0
    plus = 1000
    length = len(y[0]) - 1000
    limit=(-1500,2000)

    while start < length:
        time = [x + start for x in range(plus)]

        plt.subplot(311)
        plt.ylim(limit)
        plt.plot(time, y[0][start:start + plus], linewidth=2)
        plt.title("ButterFly \n order:" + str(order) + "  fs_cut:" + str(freq_cut) + "\n  GryoX(deg/s)", fontsize=8)
        plt.grid()
        # plt.legend()
        plt.subplots_adjust(hspace=0.5)

        plt.subplot(312)
        plt.ylim(limit)
        plt.plot(time, y[1][start:start + plus], linewidth=2)
        plt.title("GroyY(deg/s)", fontsize=8)
        plt.grid()
        # plt.legend()
        plt.subplots_adjust(hspace=0.5)

        plt.subplot(313)
        plt.ylim(limit)
        plt.plot(time, y[2][start:start + plus], linewidth=2)
        plt.title("GroyZ(deg/s)", fontsize=8)
        plt.xlabel('Time [sec]', fontsize=8)
        plt.grid()
        # plt.legend()
        plt.subplots_adjust(hspace=0.5)
        plt.savefig("../imag/butter" + str(i), dpi=1000)
        plt.clf()
        i += 1
        start += plus
