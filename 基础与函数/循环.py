# -*- conding: utf-8 -*-
name = ['小宋', '小小', '小黑']
for names in name:
    print('他们名字是', names)

sum = 0
for X in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + X
    print(sum)
print("1到10相加=", sum)

sum101 = 0
for y in range(101):  #rang()等于[0,1,2,......,100]
    sum101 = sum101 + y
print(sum101, list(range(101)))
print()

sum100 = 0
n = 0
while n < 101:
    sum100 = sum100 + n
    n = n + 1
print("sum100=", sum100)

n1 = 0
while n1 < 99:
    if n1 > 10:
        print(n1)
        break  #结束循环，退出整个循环
    n1 = n1 + 1
print("END", n1)

n3 = 0
while n3 < 10:
    n3 = n3 + 1
    if n3 % 2 == 0:  # 如果n是偶数，执行continue语句
        continue  # continue语句会直接继续下一轮循环，后续的print()语句不会执行
    print(n3)

