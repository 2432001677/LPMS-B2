from Project import np

'''
文件对象
获得csv内的数据
'''


class Data:

    def __init__(self, file):
        file = "../../data/" + file
        self.file = file
        self.data = []

        print("读取文件中")
        for i in range(9):
            self.data.append(np.loadtxt(file, delimiter=',', usecols=(i + 3,), skiprows=1))

        for i in range(4):
            self.data.append(np.loadtxt(file, delimiter=',', usecols=(i + 15,), skiprows=1))

        print("读取成功")

    def get_acc(self):
        return self.data[0:3]

    def get_gyro(self):
        return self.data[3:6]

    def get_mag(self):
        return self.data[6:9]

    def get_quat(self):
        return self.data[9:]
