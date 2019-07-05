#!/usr/bin/env python
#-*- coding:utf-8 -*-
from types import FunctionType, MethodType

def func(x):
    return x+1
s = lambda a:10+a*0.2
print(type(s))
a=func
print(isinstance(a,FunctionType))
a=[1,2,2.3,4,3.4]
a.sort()
for i in a:
    print(i)