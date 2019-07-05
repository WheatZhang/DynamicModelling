#!/usr/bin/env python
#-*- coding:utf-8 -*-
import re

test_str = "_x_da[*,1]"
matchObj = re.search( r'^(.*)\[', test_str).group(1)
matchIndex = re.search( r'\[(.*)\]', test_str).group(1)
print(matchObj)
print(matchIndex)

print(str({1:"34"}))