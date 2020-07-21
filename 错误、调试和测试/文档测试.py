#!/usr/bin/env
# -*- coding:utf-8 -*-
import re
m = re.search('(?<=abc)def','abcdef')   #而此处的(?<=…) 的功能是，判断（当前位置）之前的内容是什么。
#(?<=…):
# 匹配字符串的当前位置，它的前面匹配 … 的内容到当前位置。这叫:dfn:positive lookbehind assertion （正向后视断定）。 
#(?<=abc)def 会在 'abcdef' 中找到一个匹配，因为后视会往后看3个字符并检查是否包含匹配的样式。
# 包含的匹配样式必须是定长的，意思就是 abc 或 a|b 是允许的，但是 a* 和 a{3,4} 不可以。
# 注意以 positive lookbehind assertions 开始的样式，如 (?<=abc)def ，并不是从 a 开始搜索，
# 而是从 d 往回看的。你可能更加愿意使用 search() 函数，而不是 match() 函数：
m.group()


class Dict(dict):
    '''
    Simple dict but also support access as x.y style.

    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
        ...
    KeyError: 'empty'
    >>> d2.empty
    Traceback (most recent call last):
        ...
    AttributeError: 'Dict' object has no attribute 'empty'
    '''
    def __init__(self, **kw):
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

if __name__=='__main__':
    import doctest
    doctest.testmod()
