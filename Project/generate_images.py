from Project import plt, mkdir, exists


def generate_images(y, freq_cut, order, file):
    if not exists("../imag"):
        mkdir("../imag")
    start = i = 0
    plus = 1000
    length = len(y[0]) - 1000
    limit = (-1500, 2000)

    print("开始生成图片")
    while start < length:
        time = [x + start for x in range(plus)]

        plt.subplot(311)  # x轴角速度子图
        plt.ylim(limit)  # 设置y轴取值范围
        plt.plot(time, y[0][start:start + plus], linewidth=2)  # 时间为横坐标, 数据为纵坐标
        plt.title(file[:-4] + " \n order:" + str(order) + "  fs_cut:" + str(freq_cut) + "\n  GryoX(deg/s)",
                  fontsize=8)  # 设置标题
        plt.grid()  # 显示网格
        # plt.legend()
        plt.subplots_adjust(hspace=0.5)  # 调整子图间距

        plt.subplot(312)  # y轴
        plt.ylim(limit)
        plt.plot(time, y[1][start:start + plus], linewidth=2)
        plt.title("GroyY(deg/s)", fontsize=8)
        plt.grid()
        # plt.legend()
        plt.subplots_adjust(hspace=0.5)

        plt.subplot(313)  # z轴
        plt.ylim(limit)
        plt.plot(time, y[2][start:start + plus], linewidth=2)
        plt.title("GroyZ(deg/s)", fontsize=8)
        plt.xlabel('Time [sec]', fontsize=8)
        plt.grid()
        # plt.legend()
        plt.subplots_adjust(hspace=0.5)
        plt.savefig("../imag/" + file[:-4] + " " + str(i), dpi=1000)
        print("图片" + str(i) + " ...", end='  ')
        plt.clf()
        i += 1
        start += plus

    print("\n图片生成结束")

