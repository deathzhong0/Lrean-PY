#!/usr/bin/env python 
# -*- coding:utf-8 -*-




class Dict(dict):
    def __init__(self,**kw):
        super().__init__(**kw)
    
    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self,key,value):
        self[key] = value

d = Dict(a=1, b=2)
d['a']
d.a
print(d.a)

#为了编写单元测试，我们需要引入Python自带的unittest模块，编写mydict_test.py如下：
import unittest

class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a = 1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key,'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'],'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_arrterror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == '__main__':
    unittest.main()

#练习

#对Student类编写单元测试，结果发现测试不通过，请修改Student类，让测试通过：
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 60:
            return 'B'
        if self.score >= 80:
            return 'A'
        return 'C'
