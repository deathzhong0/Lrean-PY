# -*- coding:utf-8 -*-
def os(x):
    return x + x


print(os(2))


def os1(x, n=3):
    y = 1
    while n > 0:
        n = n - 1
        y = y * x
    return y


print(os1(2))


def MT(name, age):
    print(name)
    print(age)


print(MT(1, 2))
print(1)


def calc(*number):
    q = 0
    for n in number:
        q = q + n * n
    return q


print(calc(1, 2))

ff = [1, 2, 3]
print(calc(*ff))


def person(name, **other):
    print('name:', name, "other:", other)


print(person('DZ', city='趋势'))

其他 = {'我的妈呀': 'wdmy', '额么么么': 'emmm'}
print(person('DZ', **其他))


def person1(name, *, s):  #加*能只显示s=的内容；命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
    print('name:', name, "other:", s)


print(person1("11", s="ss"))


def product(result1, *number1):
    result = result1

    for x in number1:
        result = x * result

    return result


# 测试

print('product(5) =', product(5))
print('product(5, 6) =', product(5, 6))
print('product(5, 6, 7) =', product(5, 6, 7))
print('product(5, 6, 7, 9) =', product(5, 6, 7, 9))
if product(5) != 5:
    print('测试失败!')
elif product(5, 6) != 30:
    print('测试失败!')
elif product(5, 6, 7) != 210:
    print('测试失败!')
elif product(5, 6, 7, 9) != 1890:
    print('测试失败!')
else:
    try:
        product()
        print('测试失败!')
    except TypeError:
        print('测试成功!')