from project import plt


def show(data, y, freq_cut, order):
    plt.subplot(311)
    plt.plot(data[0][20000:21000], 'b-', label='data')
    plt.plot(y[0][20000:21000], 'g-', linewidth=2, label='filtered data')
    plt.title("ButterFly \n order:" + str(order) + "  fs_cut:" + str(freq_cut)+"\n  GryoX(deg/s)")
    plt.xlabel('Time [sec]')
    plt.grid()
    plt.legend()
    plt.subplots_adjust(hspace=0.35)

    plt.subplot(312)
    plt.plot(data[1][20000:21000], 'b-', label='data')
    plt.plot(y[1][20000:21000], 'g-', linewidth=2, label='filtered data')
    plt.title("GroyY(deg/s)")
    plt.xlabel('Time [sec]')
    plt.grid()
    plt.legend()
    plt.subplots_adjust(hspace=0.35)

    plt.subplot(313)
    plt.plot(data[2][20000:21000], 'b-', label='data')
    plt.plot(y[2][20000:21000], 'g-', linewidth=2, label='filtered data')
    plt.title("GroyZ(deg/s)")
    plt.xlabel('Time [sec]')
    plt.grid()
    plt.legend()
    plt.subplots_adjust(hspace=0.35)

    plt.show()


