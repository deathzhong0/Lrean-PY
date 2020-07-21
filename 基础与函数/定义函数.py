# -*- coding: utf-8 -*-
def app():
    print('X =100')


print(app())


def my_ab(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_ab(88))


def nop():
    pass  #站位符，没想好可以先占着让代码跑起来


from asd import my_abs  #调用当前目录下其他文件（此处文件名为asd）的函数
try:
    print(my_abs("A"))
except EOFError:
    print('ss')

import math  #导入math库


def move(x, y, step, angle=0):  #能返回多个值
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 60, math.pi / 6)
print(x, y)

#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程 ax^2+bx+c=0 的两个解
import math


def quadratic(a, b, c):
    if not isinstance(a, (int, float)) :
        if not isinstance(b, (int, float)):
            if not isinstance(c, (int, float)):
                raise TypeError("a、b、c不是数字")
            raise TypeError("a、b不是数字")
        if not isinstance(c, (int, float)):
            raise TypeError("a、c不是数字")
        raise TypeError("a不是数字")
    if not isinstance(b, (int, float)):
        if not isinstance(c, (int, float)):
                raise TypeError("b、c不是数字")
        raise TypeError("b不是数字")
    if not isinstance(c, (int, float)):
        raise TypeError("c不是数字")
    if a == 0:
        if b == 0:
            if c == 0:
                return "全体实数"
            else:
                return "无实数根"
        else:
            x1 = -c / b
            x2 = x1
            return x1, x2
    else:
        sqrt = b**2 - (4 * a * c)
        if sqrt < 0:
            return "无实根"
        x1 = (-b + math.sqrt(sqrt)) / (2 * a)
        x2 = (-b - math.sqrt(sqrt)) / (2 * a)
        return x1, x2


# 测试:
print('quadratic(2, 3, 1) =', quadratic(9,2,8))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))

if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')