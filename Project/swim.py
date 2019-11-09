from Project import np
from Project import sys

sys.setrecursionlimit(1000000)


class Swim:

    def __init__(self, y):
        self.acc = self.gyro = self.mag = self.quat = None
        self.sum_distance = 0  # 总距离
        self.number = 0
        self.all_time = 0
        self.arm_stroke = 2
        self.once_time = 0
        self.pool = 0
        self.time_frame_interval = 500  # 时间帧覆盖窗口大小
        self.flag = 1000
        self.flag2 = 500
        self.name = None
        self.time_point_list = []
        self.example = []
        self.start_time = 0
        self.example = y
        self.get_frequency()
        self.tst()

    # free/buffer 500 1000 500
    # back 600 700 400
    # breast 600 400 220 有误差，无法对比

    def get_frequency(self):
        start_time = self.start_time
        end_time = len(self.example)
        max_time_interval = 1000
        all_time = 0
        arm_stroke = self.arm_stroke

        time_frame_interval = self.time_frame_interval
        increment_time_frame = 25  # 时间帧向前滑动距离
        flag = self.flag
        flag2 = self.flag2
        sum_distance = end_time - self.start_time
        time_point_list = self.time_point_list
        while start_time < end_time - time_frame_interval:
            a=np.array(self.example[start_time:start_time + time_frame_interval])
            x = np.ptp(a)
            if x > flag:
                max_value = np.amax(self.example[start_time:start_time + time_frame_interval])
                for i in range(time_frame_interval):
                    if self.example[start_time + i] == max_value and self.example[start_time + i] > flag2:
                        time_point_list.append(start_time + i)
                        break

                start_time += time_frame_interval
                while self.example[start_time] > flag2:
                    start_time += increment_time_frame
                    if start_time>end_time:
                        break
            else:
                start_time += increment_time_frame

        if len(time_point_list) > 1:
            self.all_time = time_point_list[len(time_point_list) - 1] - time_point_list[0]
            self.number = len(time_point_list)
            self.once_time = self.all_time / self.number
        # 计算所有时间间隔，取平均
        #    self.pool = self.number * self.arm_stroke

        # for i in range(len(time_point_list)):
        #     if time_point_list[i+1]-time_point_list[i]>2*once_time:
        #         print(i)#转向处
        #         break
        # self.time_point_list.clear()
        self.time_point_list = time_point_list

        return time_point_list

    def tst(self):
        if len(self.time_point_list) > 5:
            if np.amax(
                    self.example[self.time_point_list[0]:self.time_point_list[len(self.time_point_list) - 1]]) > 1000:
                self.name = "butterfly"
            else:
                if np.amax(self.example[
                           self.time_point_list[0]:self.time_point_list[len(self.time_point_list) - 1]]) > 500:
                    self.name = "freestyle"
        else:
            self.time_frame_interval = 600  # 时间帧覆盖窗口大小
            self.flag = 700
            self.flag2 = 400
            self.time_point_list.clear()

            self.get_frequency()
            if len(self.time_point_list) > 5:
                if np.amax(self.example[
                           self.time_point_list[0]:self.time_point_list[len(self.time_point_list) - 1]]) > 500:
                    self.name = "backstroke"
            else:
                self.time_frame_interval = 600  # 时间帧覆盖窗口大小
                self.flag = 400
                self.flag2 = 300
                self.time_point_list.clear()
                self.get_frequency()
                if len(self.time_point_list) > 1:
                    if np.amax(self.example[
                               self.time_point_list[0]:self.time_point_list[len(self.time_point_list) - 1]]) < 700:
                        self.name = "breaststroke"

    def print_inf(self):
        print(self.number)  # 划臂次数
        print(self.all_time)  # 总时间
        print(self.once_time)  # 单词划臂时间
        print(self.pool)  # 游泳距离
        print(self.name)
