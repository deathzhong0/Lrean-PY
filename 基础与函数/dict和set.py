#-*- coding: utf-8 -*-
a = {'大山':'@','黄河':3,'蓝天':4}   #{}为字典类型
print('输出大山的值',a['大山'])
print("判断大山是否在集合",'大山'in a)
print('获取大山集合的',a.get('大山'))
print('删除大山的集合里的值',a.pop('大山'))    # 删除key
print(a)
b = set([5,2,3,3])  #创建一个无序无重复的集
b.add(4)    #增加一个4
b.remove(2) #删除一个2
print('b集合=',b)
c = ['5','2','A']
c.sort()
print(c) #排序，默认升序
d = 'Abc'
e=d.replace('A','a')    #替换，但不会改变原本的字符
print(d)
print(e)

#请问Python如何实现将列表：['a','a','b','a','b','c']输出为字典：{'a':3,'b':2,'c':1}?

L=['a', 'a', 'b', 'a', 'b', 'c'] 
dic={}
for x in L:
    dic[x]=L.count(x)   #添加每一个字典的键和值
print('列表个字符个数',dic)