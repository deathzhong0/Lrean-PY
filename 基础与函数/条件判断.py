# -*- coding: utf-8 -*-
age = input('请输入年龄\n')
a = str(age).isdigit()  # 判断是否为数字
if a is True:
    age1 = int(age)
    if age1 >= 30:

        print('大于30')
    elif age1 >= 20:
        print('大于20')

    else:

        print('小于30')
else:
    print('请输入正常的年龄')

height = float(input('请输入身高(单位m)'))
weight = float(input('请输入体重（单位kg）'))
BIM = float(weight / (height**2))

if BIM < 18.5:
    print('过轻')
elif 18.5 <= BIM <= 25:
    print('正常')
elif 25 < BIM <= 28:
    print('过重')
elif 28 < BIM <= 32:
    print('肥胖')
elif BIM > 32:
    print('严重肥胖')
else:
    print("请输入正常的体重身高")
print('你的BIM=%.2f' % (BIM))
