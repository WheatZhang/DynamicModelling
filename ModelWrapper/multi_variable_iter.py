#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np

def get_target_range(domain, roc):
    if not isinstance(domain, np.ndarray):
        domain = np.array(domain)
    if not isinstance(roc, np.ndarray):
        roc = np.array(roc)
    div_num = roc.shape[1]
    result = np.zeros(shape=(roc.shape[0],2))
    for i in range(roc.shape[0]):
        current_length = 0
        max_length = 0
        for j in range(div_num):
            if roc[i,j] == 1:
                current_length += 1
                if current_length > max_length:
                    max_length = current_length
            else:
                current_length = 0
        if max_length == 0:
            result[i,0]=-999
            result[i, 1] = -999
        else:
            left_index = 0
            right_index= -1
            current_length = 0
            for j in range(div_num):
                if roc[i, j] == 1:
                    current_length += 1
                    right_index+=1
                else:
                    if current_length == max_length:
                        break
                    else:
                        right_index = j
                        left_index = j+1
                        current_length = 0
            result[i, 0] = domain[i,0]+(domain[i,1]-domain[i,0])/(div_num-1)*left_index
            result[i, 1] = domain[i,0]+(domain[i,1]-domain[i,0])/(div_num-1)*right_index
    return result



def iter_grid(domain, iter_num):
    if isinstance(iter_num, int):
        iter_num = np.array([iter_num])
    if not isinstance(domain, np.ndarray):
        domain = np.array(domain)
    if not isinstance(iter_num, np.ndarray):
        iter_num = np.array(iter_num)
    if domain.ndim == 1:
        domain=np.array([domain])
    #如果只有一维，则要单算
    if len(iter_num) == 1:
        data = domain[0, 0]
        iter_status = 1
        increment = (domain[0,1]-domain[0,0])/(iter_num[0]-1)
        while True:
            yield data
            if iter_status == iter_num[0]:
                break
            else:
                data+=increment
            iter_status += 1
    elif len(iter_num) > 1:
        iter_status = [1 for x in range(len(iter_num))]
        data = [domain[x, 0] for x in range(len(iter_num))]
        increment = [0 for x in range(len(iter_num))]
        for i in range(len(increment)):
            increment[i] = (domain[i,1]-domain[i,0])/(iter_num[i]-1)
        last_var = len(iter_num) - 1
        while True:
            yield data
            if iter_status[last_var] < iter_num[last_var]:
                data[last_var]+=increment[last_var]
                iter_status[last_var] += 1
            else:
                full_var = len(iter_num)-1
                for i in range(1,len(iter_num)):
                    if iter_status[last_var-i] == iter_num[last_var-i]:
                        full_var-=1
                    else:
                        break
                if full_var == 0:
                    break
                iter_status[full_var-1] += 1
                data[full_var-1]+=increment[full_var-1]
                for i in range(full_var, len(iter_num)):
                    iter_status[i] = 1
                    data[i] = domain[i,0]
    else:
        raise Exception("the dimension of iter_num is incorrect.")

# test
# domain=[[1,3],[4,6],[7,8]]
# iter_num = [3,3,2]
# iter1 = iter_grid(domain, iter_num)
# for x in iter1:
#     print(x)
#
# iter2 = iter_grid([1,5], 5)
# for x in iter2:
#     print(x)
# print(get_target_range(domain,[[0,1,1,0],[1,1,1,1],[0,0,0,0]]))