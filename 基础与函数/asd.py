
def my_abs(x):
    if not isinstance(x,(int,float)):   #检测是否是int、float类型
        raise TypeError('!哈哈!')   #出错时返回
    if x >= 0:
        return x
    else:
        return -x
print(my_abs(88))

