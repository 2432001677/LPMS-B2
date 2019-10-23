from Project import np


class Swim:
    acc = gyro = mag = quat = None
    sum_distance = 0  # 总距离


    def get_frequency(self, y,start_time, end_time):
        max_time_interval = 1000;
        all_time = 0
        arm_stroke = 1.5
        time_frame_interval = 500  # 时间帧覆盖窗口大小
        increment_time_frame = 25  # 时间帧向前滑动距离
        flag = 900
        sum_distance = end_time-start_time
        time_point_list = []
        while start_time < end_time - time_frame_interval:
            x = np.ptp(y[start_time:start_time + time_frame_interval])
            if x > flag:
                max_value=np.amax(y[start_time:start_time + time_frame_interval])
                for i in range(time_frame_interval):
                    if y[start_time+i]==max_value and y[start_time+i]>500:
                        time_point_list.append(start_time+i)

                start_time += time_frame_interval
                while y[start_time] > 500:
                    start_time += increment_time_frame
            else:
                start_time += increment_time_frame


        #all_time = time_point_list[len(time_point_list)-1]-time_point_list[0]
        #number = len(time_point_list)
        #once_time = all_time / number
        # 计算所有时间间隔，取平均
        # pool = number * arm_stroke
        # print(number)#划臂次数
        # print(all_time)#总时间
        # print(once_time)#单词划臂时间
        # print(pool)#游泳距离
        print(len(time_point_list))
        # for i in range(len(time_point_list)):
        #     if time_point_list[i+1]-time_point_list[i]>2*once_time:
        #         print(i)#转向处
        #         break
        return time_point_list
