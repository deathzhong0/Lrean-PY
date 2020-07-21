# -*- coding: utf-8 -*-
laojia = ['house', 'tree', 'sky']
laojia.append('mountain')  # 增加列表个数
laojia.insert(2, 'lake')  # 指定插入位置
print(laojia[0])
print(laojia[-2])

print(len(laojia))
print(laojia)
laojia.pop(1)  # 删除指定位置的元素
print(laojia)
laojia[2] = '666'  # 替换指定位置的元素
print(laojia)

laojia = (1,)  # tuple类型不可改


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])
print('元组=', laojia)
