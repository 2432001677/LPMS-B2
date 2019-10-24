from Project import np


class Swim:
    def __init__(self, y, start_time, end_time):
        self.acc = self.gyro = self.mag = self.quat = None
        self.sum_distance = 0  # 总距离
        self.get_frequency(y, start_time, end_time)

    def get_frequency(self, y, start_time, end_time):
        max_time_interval = 1000
        all_time = 0
        arm_stroke = 1.5
        time_frame_interval = 500  # 时间帧覆盖窗口大小
        increment_time_frame = 25  # 时间帧向前滑动距离
        flag = 900
        self.sum_distance = end_time - start_time
        time_point_list = []
        while start_time < end_time - time_frame_interval:
            x = np.ptp(y[start_time:start_time + time_frame_interval])
            if x > flag:
                max_value = np.amax(y[start_time:start_time + time_frame_interval])
                for i in range(time_frame_interval):
                    if y[start_time + i] == max_value and y[start_time + i] > 500:
                        time_point_list.append(start_time + i)

                start_time += time_frame_interval
                while y[start_time] > 500:
                    start_time += increment_time_frame
            else:
                start_time += increment_time_frame

        self.all_time = time_point_list[len(time_point_list) - 1] - time_point_list[0]  # 总时间
        self.number = len(time_point_list)  # 划臂次数
        self.once_time = all_time / self.number  # 单词划臂时间
        # 计算所有时间间隔，取平均
        self.pool = self.number * arm_stroke  # 游泳距离
        for i in range(len(time_point_list)):
            if time_point_list[i + 1] - time_point_list[i] > 2 * self.once_time:
                print(i)  # 转向处
                break
