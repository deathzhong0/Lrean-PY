'Hello, {0}, 成绩提升了 {1:.1f}%'.format('小明', 17.125)  # {:}截取字符串中的一部分，遵循左闭右开原则
print('{} {}'.format('hello', 'world'))  # 不带字段

print('{0} {1}'.format('hello', 'world'))  # 带数字编号

print('{0} {1} {0}'.format('hello', 'world'))  # 打乱顺序

print('{1} {1} {0}'.format('hello', 'world'))

print('{a} {tom} {a}'.format(tom='hello', a='world'))  # 带关键字


s1 = 72
s2 = 85
r = ((s2-s1)/s1)*100
print('他比上次增长了%.1f%%' % (r))
print('他比上次提升了{0:.3}%'.format(r))
print('{0}{1:.1f}%'.format('小明成绩提升了', r))    #{0}指小明成绩提升了，{1:.1f}指r的值并且浮点数保留小数点一位
