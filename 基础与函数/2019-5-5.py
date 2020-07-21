x = input("输入x的值")
y = input("输入y的值")
a = str(x).isdigit()  # 判断是否为数字
b = str(y).isdigit()

if str(x).isdigit() is False or str(y).isdigit() is False:
    print("请输入数字，SB")
else:
    print("x*y=", int(x)*int(y))

print('''"ID(x)=%s",id(x)

"ID(y)=%d",id(y)''' % (id(x), id(y)))  # 字符串格式化,打印赋值id
