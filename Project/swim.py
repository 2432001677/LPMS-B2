class Swim:
    acc=gyro=mag=quat=None
    sum_distance=0  # 总距离


    def get_frequency(self,start_time,end_time):
        time_frame_interval=300  # 时间帧覆盖窗口大小
        increment_time_frame=25  # 时间帧向前滑动距离


