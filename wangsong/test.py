from Project import np

#np.ptp(a)
#移动窗口
def fun(a):
    value=10
    list =[]
    size=250#窗口大小
    l=0#左下标
    r=l+size#右下标
    while l<a.size():
        x=np.ptp(a[l:r])
        if x>value :
            list.append(l)
            l=r
        l=l+1
    number=len(list)
    for t in list:
        #计算所有时间间隔，取平均

#根据身高体重估单次划臂距离
#距离*number与泳池距离比对



