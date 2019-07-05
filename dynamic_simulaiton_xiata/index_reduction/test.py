#!/usr/bin/env python
#-*- coding:utf-8 -*-

import load_initials

list = [0,
        1,
        2.0,
        3.0,
        5.0,
        10,
        11,
        12,
        13,
        14,
        15,
        16]
print(load_initials.get_lower_bound_index(0,list))
print(load_initials.get_lower_bound_index(0.0,list))
print(load_initials.get_lower_bound_index(4,list))
print(load_initials.get_lower_bound_index(3,list))
print(load_initials.get_lower_bound_index(9.9,list))
print(load_initials.get_lower_bound_index(11,list))
