from pyomo.environ import *
from pyomo.dae import *
import re

def to_template(model, file_name):
    all_attr = dir(model)
    f = open(file_name, "w")
    for attr in all_attr:
        if isinstance(getattr(model, attr), pyomo.core.base.var.SimpleVar):
            f.write(attr+'\t')
            f.write(str(getattr(model,attr)._value))
            f.write('\n\n')
        elif isinstance(getattr(model, attr), pyomo.core.base.var.IndexedVar):
            f.write(attr + '\n')
            for key, value in getattr(model, attr)._data.items():
                f.write(str(key) + '\t')
                f.write(str(value._value)+'\n')
            f.write('\n')
        elif isinstance(getattr(model, attr), pyomo.dae.DerivativeVar):
            f.write(attr + '\n')
            for key, value in getattr(model, attr)._data.items():
                f.write(str(key) + '\t')
                f.write(str(value._value) + '\n')
            f.write('\n')
    f.close()

def load_init_from_template(model, file_name):
    for name, value in load_general_txt_init(model, file_name):
        set_initials(model, name, value)

def load_general_txt_init(model, file_name):
    status = "Ready"
    file = open(file_name)
    for line in file:
        line_split = line.split('\t')
        # print(line_split)
        for i in range(len(line_split)):
            line_split[i] = line_split[i].strip()
        if status == "Ready":
            if len(line_split) == 0:
                continue
            elif len(line_split) == 1:
                if line_split[0] == "":
                    continue
                else:
                    status = "IndexedVarStart"
                    var_name = line_split[0]
                    dict = {}
                    continue
            elif len(line_split) == 2:
                if line_split[0] == "":
                    continue
                elif line_split[1] == "":
                    status = "IndexedVarStart"
                    var_name = line_split[0]
                    dict = {}
                    continue
                else:
                    yield line_split[0], float(line_split[1])
                    continue
            else:
                raise Exception("Wrong template format.")
        elif status == 'IndexedVarStart':
            if len(line_split) == 0:
                yield var_name, dict
                status = "Ready"
                continue
            elif len(line_split) == 1:
                if line_split[0] == "":
                    yield var_name, dict
                    status = "Ready"
                    continue
                else:
                    yield var_name, dict
                    status = "IndexedVarStart"
                    var_name = line_split[0]
                    continue
            elif len(line_split) == 2:
                if line_split[0] == "":
                    yield var_name, dict
                    status = "Ready"
                    continue
                else:
                    str = line_split[0]
                    if str[0] == "\"" or str[0] == "\'":
                        str = str[1:-1]
                    if str[0] == '(':
                        dict[eval(str)] = float(line_split[1])
                    else:
                        if str.isdigit():
                            dict[int(str)] = float(line_split[1])
                        elif re.match(r'[a-zA-Z]',str) == None:
                            if type(eval(str)) == float:
                                dict[float(str)] = float(line_split[1])
                            else:
                                raise Exception("Wrong index format.")
                        else:
                            dict[str] = float(line_split[1])
            else:
                raise Exception("Wrong template format.")
    file.close()

def set_initials(model, var_name, initial_value):
    all_attr = dir(model)
    if var_name in all_attr:
        if isinstance(initial_value, dict):
            if (not isinstance(getattr(model, var_name),pyomo.core.base.var.IndexedVar))\
                and (not isinstance(getattr(model, var_name),pyomo.dae.DerivativeVar)):
                raise Exception("%s is not a IndexedVar or a DerivativeVar" % var_name)
            for key, value in initial_value.items():
                getattr(model, var_name)._data[key]._value = value
            getattr(model, var_name)._value_init_value = initial_value
        else:
            if not isinstance(getattr(model, var_name),pyomo.core.base.var.SimpleVar):
                raise Exception("%s is not a SimpleVar" % var_name)
            getattr(model, var_name)._value = initial_value
            getattr(model, var_name)._value_init_value = initial_value
    else:
        raise Exception("There is no variable called:%s"%var_name)

def set_initials_partial_index(model, var_name, tag_index, initial_value):
    all_attr = dir(model)
    if not isinstance(getattr(model, var_name), pyomo.core.base.var.IndexedVar):
        if not isinstance(getattr(model, var_name), pyomo.dae.DerivativeVar):
            raise Exception("Wrong type of member. %s is not a indexed var."%var_name)
    if var_name in all_attr:
        if tag_index == [] or tag_index == None:
            for key in getattr(model, var_name)._data.keys():
                getattr(model, var_name)._data[key]._value = initial_value
        else:
            for key in getattr(model, var_name)._data.keys():
                matched_item = []
                for i, element in enumerate(tag_index):
                    matched_item.append(key[element])
                if len(matched_item) == 1:
                    matched_item = matched_item[0]
                else:
                    matched_item = tuple(matched_item)
                getattr(model, var_name)._data[key]._value = initial_value[matched_item]
            getattr(model, var_name)._value_init_value = None
    else:
        raise Exception("There is no variable called:"+var_name)

def load_naive_var_init(model, filename):
    for name, value in load_general_txt_init(model, filename):
        if type(value) == dict:
            if type(list(value.keys())[0]) == tuple:
                size = len(list(value.keys())[0])
            else:
                size = 1
            tag_index = []
            for i in range(size):
                tag_index.append(i+1)
            set_initials_partial_index(model, name, tag_index, value)
        else:
            set_initials_partial_index(model, name, None, value)

