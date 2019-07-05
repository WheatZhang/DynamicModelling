#!/usr/bin/env python
#-*- coding:utf-8 -*-

def gener():
    i = 1
    while i < 10:
        yield i,i+1
        i = i+1

for i,j in gener():
    print(i)