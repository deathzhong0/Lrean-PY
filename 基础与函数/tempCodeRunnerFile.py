x = input("输入x的值")
y = input("输入y的值")
a = str(x).isdigit()
b = str(y).isdigit()
if str(x).isdigit() == False or str(y).isdigit() == False:
    print("SB")
else:
    print("x*y=", float(x)*float(y))
print("ID(x)=", id(x)'\t', "ID(y)=", id(y))
