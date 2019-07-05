#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
from pyomo.dae import *
import csv
def load_initials_from_csv(model,filepath):
    csv_file = csv.reader(open(filepath, 'r'))
    status = 0
    tags=[]
    for l in csv_file:
        line = []
        for elem in l:
            if elem != '':
                line.append(elem)
        for i in range(len(line)):
            line[i] = line[i].strip()
        if len(line) == 0 or line[0].startswith('#'): # 井号为注释
            if status == 1:
                setup_indexed_var(model, var_name, tags,dict)
            elif status == 3:
                setattr(model, var_name, Var(getattr(model, tags[0]), getattr(model, tags[1]), rule=dict))
            status = 0
            continue
        if line[0].startswith(':'):
            if status == 1:
                setup_indexed_var(model, var_name, tags,dict)
            elif status == 3:
                setattr(model, var_name, Var(getattr(model, tags[0]), getattr(model, tags[1]), rule=dict))
            if line[0].startswith(':VAR'):
                var_name = line[1]
                tags = line[2:]
                dict = {}
                status = 1
            elif line[0] == ':TABLE':
                var_name = line[1]
                tags = line[2:4]
                dict = {}
                status = 2
            else:
                raise Exception('Unidentified Tag')
            continue
        if status == 0:
            var_name = line[0]
            value = float(line[1])
            setattr(model, var_name,Var(initialize=value))
        elif status == 2:
            tag2 = line
            status = 3
            for j in range(len(tag2)):
                if tag2[j].isdigit():
                    tag2[j] = int(tag2[j])
        elif status == 1:
            if len(tags) == 0:
                raise Exception('The index must be greater than 0')
            elif len(tags) == 1:
                key = line[0]
                if key.isdigit():
                    key = int(key)
                dict[key] = float(line[1])
            else:
                key = line[:(len(line) - 1)]
                for j in range(len(key)):
                    if key[j].isdigit():
                        key[j] = int(key[j])
                key = tuple(key)
                dict[key] = float(line[-1])
        elif status == 3:
            tag1 = line[0]
            if tag1.isdigit():
                tag1 = int(tag1)
            for j in range(len(tag2)):
                key = (tag1, tag2[j])
                dict[key] = float(line[j + 1])
    if status == 1:
        setup_indexed_var(model, var_name, tags,dict)
    elif status == 3:
        setattr(model, var_name, Var(getattr(model, tags[0]), getattr(model, tags[1]), rule=dict))

def setup_indexed_var(model,var_name, tags,dict):
    if len(tags) == 0:
        raise Exception("Logic error")
    elif len(tags) == 1:
        setattr(model, var_name, Var(getattr(model, tags[0]), rule=dict))
    elif len(tags) == 2:
        setattr(model, var_name, Var(getattr(model, tags[0]), getattr(model, tags[1]), rule=dict))
    elif len(tags) == 3:
        setattr(model, var_name, Var(getattr(model, tags[0]), getattr(model, tags[1]), getattr(model, tags[2]), rule=dict))
    elif len(tags) == 4:
        setattr(model, var_name,
                Var(getattr(model, tags[0]), getattr(model, tags[1]), getattr(model, tags[2]), getattr(model, tags[3]),
                    rule=dict))
    else:
        raise Exception("Too many indexes")