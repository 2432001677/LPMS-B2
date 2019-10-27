from Project import np


class Swim:
    acc = gyro = mag = quat = None
    sum_distance = 0  # 总距离
    number=0
    all_time=0
    arm_stroke=1.5
    once_time=0
    pool=0
    time_frame_interval = 500  # 时间帧覆盖窗口大小
    flag = 1000
    flag2 = 500
    name=None
    time_point_list = []
    example=[]
    start_time=0
    end_time=0

    # free/buffer 500 1000 500
    #back 600 700 400
    # breast 600 400 220 有误差，无法对比

    def get_frequency(self, y,start_time, end_time):
        self.example=y
        self.start_time=start_time
        self.end_time=end_time
        max_time_interval = 1000;
        all_time = 0
        arm_stroke = self.arm_stroke

        time_frame_interval=self.time_frame_interval
        increment_time_frame = 25  # 时间帧向前滑动距离
        flag = self.flag
        flag2=self.flag2
        sum_distance = end_time-start_time
        time_point_list = self.time_point_list
        while start_time < end_time - time_frame_interval:
            x = np.ptp(y[start_time:start_time + time_frame_interval])
            if x > flag:
                max_value=np.amax(y[start_time:start_time + time_frame_interval])
                for i in range(time_frame_interval):
                    if y[start_time+i]==max_value and y[start_time+i]>flag2:
                        time_point_list.append(start_time+i)

                start_time += time_frame_interval
                while y[start_time] > flag2:
                    start_time += increment_time_frame
            else:
                start_time += increment_time_frame

        if len(time_point_list)>1:
            self.all_time = time_point_list[len(time_point_list)-1]-time_point_list[0]
            self.number = len(time_point_list)
            self.once_time = self.all_time / self.number
        # 计算所有时间间隔，取平均
        #    self.pool = self.number * self.arm_stroke


        # for i in range(len(time_point_list)):
        #     if time_point_list[i+1]-time_point_list[i]>2*once_time:
        #         print(i)#转向处
        #         break
        #self.time_point_list.clear()
        self.time_point_list=time_point_list

        return time_point_list

    def tst(self):

        if len(self.time_point_list)>5 :
            if np.amax(self.example[self.time_point_list[0]:self.time_point_list[len(self.time_point_list)-1]])>1000:
                self.name="butterfly"
            else:
                if np.amax(self.example[
                           self.time_point_list[0]:self.time_point_list[len(self.time_point_list) - 1]]) > 500:
                    self.name="freestyle"
        else:
            self.time_frame_interval = 600  # 时间帧覆盖窗口大小
            self.flag = 700
            self.flag2 = 400
            self.time_point_list.clear()
            self.get_frequency(self.example,self.start_time,self.end_time)
            if len(self.time_point_list) > 5:
                if np.amax(self.example[
                           self.time_point_list[0]:self.time_point_list[len(self.time_point_list) - 1]]) > 500:
                    self.name = "backstroke"
            else:
                self.time_frame_interval = 600  # 时间帧覆盖窗口大小
                self.flag = 400
                self.flag2 = 300
                self.time_point_list.clear()
                self.get_frequency(self.example, self.start_time, self.end_time)
                if len(self.time_point_list) > 1:
                    if np.amax(self.example[
                                self.time_point_list[0]:self.time_point_list[len(self.time_point_list) - 1]]) < 700:
                         self.name = "breaststroke"

        return self.name

    def print_inf(self):
        print(self.number)  # 划臂次数
        print(self.all_time)  # 总时间
        print(self.once_time)  # 单词划臂时间
        print(self.pool)  # 游泳距离
        print(self.name)
