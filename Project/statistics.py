from Project import np


def data_sta(a):
    print("GyroX:")
    write(a[0])
    print("GyroY:")
    write(a[1])
    print("GyroZ:")
    write(a[2])


def write(a):
    print("最小值："+str(np.amin(a)))#最小值
    print("最大值："+str(np.amax(a)))#最大值
    print("最大值与最小值差："+str(np.ptp(a)))#最大值与最小值差
    print("算术平均值："+str(np.mean(a)))#算术平均值
    print("标准差："+str(np.std(a)))#标准差 std=sqrt(mean((x - x.mean())**2))
    print("方差："+str(np.var(a)))#方差
    return
