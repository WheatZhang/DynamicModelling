#!/usr/bin/env python
#-*- coding:utf-8 -*-
from pyomo.environ import *
from pyomo.dae import *
from pyomo.opt import SolverStatus, TerminationCondition
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import multi_variable_iter
import math
import copy
from mpl_toolkits.mplot3d import Axes3D

class SettingItem(object):
    def __init__(self, init_value, bound, domain):
        self.type = "Param"
        self.init_value = init_value
        self.bound = bound
        self.domain = domain

class WrappedConcreteModel(object):
    def __init__(self,n_para,items_setting):
        self.model = ConcreteModel()
        self.n_para = n_para
        self.items_setting = items_setting
        self.solver = SolverFactory('ipopt')

    def get_pyomo_model(self):
        return self.model

    def set_para_name(self, para_vars):
        for key in self.items_setting.keys():
            if key in para_vars:
                self.items_setting[key].type = 'Param'
            else:
                self.items_setting[key].type = 'Var'

    def instancialize(self, para_vars):
        self.model = ConcreteModel()
        self.pre_setting(self.model)
        for key in self.items_setting.keys():
            command = ""
            if key in para_vars:
                self.items_setting[key].type = 'Param'
                command+="Param(initialize = "+str(self.items_setting[key].init_value)+")"
            else:
                self.items_setting[key].type = 'Var'
                command += "Var(initialize = " + str(self.items_setting[key].init_value) + \
                           ",bounds = "+str(self.items_setting[key].bound)+")"
            setattr(self.model,key,eval(command))
        self.post_setting(self.model)

    def solve(self):
        results = self.solver.solve(self.model, tee=False)
        if (results.solver.status == SolverStatus.ok) and (results.solver.termination_condition == TerminationCondition.optimal):
        # this is feasible and optimal
            solution = {}
            for key, value in self.items_setting.items():
                if value.type == 'Var':
                    solution[key] = getattr(self.model, key).value
            return solution
        elif results.solver.termination_condition == TerminationCondition.infeasible:
            print("Infeasible!")# do something about it? or exit?
            return -1
        else:
            print("Other error!")# something else is wrong
            return -1

    def get_range_of_converge(self,para_vars,n_div=10):
        paras = []
        vars = []
        for key in self.items_setting.keys():
            if key in para_vars:
                self.items_setting[key].type = 'Param'
                paras.append(key)
            else:
                self.items_setting[key].type = 'Var'
                vars.append(key)
        iter_domain = []
        roc = []
        for para in paras:
            iter_domain.append([self.items_setting[para].domain[0],self.items_setting[para].domain[1]])
            roc.append([1 for x in range(n_div)])
        iter_num = [n_div for k in range(len(paras))]
        for sample in multi_variable_iter.iter_grid(iter_domain, iter_num):
            for j in range(self.n_para):
                self.items_setting[paras[j]].init_value = sample[j]
            self.instancialize(para_vars)
            solution = self.solve()
            if solution == -1:
                for j in range(self.n_para):
                    index = round((sample[j]-iter_domain[j][0])/(iter_domain[j][1]-iter_domain[j][0])*(iter_num[j]-1))
                    roc[j][int(index)] = 0
                print(sample)
        return multi_variable_iter.get_target_range(iter_domain,roc)

    def two_paras_analysis(self,para_vars,n_div=10,var_vars=None):
        # para_vars中的前两个用于遍历
        paras = []
        vars = []
        if var_vars == None:
            for key in self.items_setting.keys():
                if key in para_vars:
                    self.items_setting[key].type = 'Param'
                    if key in para_vars[0:2]:
                        paras.append(key)
                else:
                    self.items_setting[key].type = 'Var'
                    vars.append(key)
        else:
            for key in self.items_setting.keys():
                if key in para_vars:
                    self.items_setting[key].type = 'Param'
                    if key in para_vars[0:2]:
                        paras.append(key)
                elif key in var_vars:
                    self.items_setting[key].type = 'Var'
                    paras.append(key)
                else:
                    self.items_setting[key].type = 'Var'
        if len(para_vars) < 2:
            raise Exception("two_paras_analysis need 2 paras.")
        if len(para_vars) != self.n_para:
            raise Exception("The number of given parameters is inconsistent with the dof.")
        iter_domain = []
        for para in paras:
            iter_domain.append([self.items_setting[para].domain[0],self.items_setting[para].domain[1]])
        iter_num = [n_div for k in range(len(paras))]
        para_samples=[]
        var_samples=[]
        iter = multi_variable_iter.iter_grid(iter_domain, iter_num)
        for sample in iter:
            for j in range(self.n_para):
                self.items_setting[paras[j]].init_value = sample[j]
            self.instancialize(para_vars)
            solution = self.solve()
            if solution != -1:
                result = []
                for j in range(len(vars)):
                    result.append(solution[vars[j]])
                var_samples.append(result)
                para_samples.append(copy.deepcopy(sample))
        rows = math.ceil(len(vars)/2)
        x = np.array(para_samples)[:,0]
        y = np.array(para_samples)[:,1]
        var_samples = np.array(var_samples)
        fig = plt.figure()
        for i in range(len(vars)):
            z = var_samples[:,i]
            ax = fig.add_subplot(rows*100+20+i+1, projection='3d')
            ax.plot_trisurf(x, y, z)
            ax.set_xlabel(paras[0])
            ax.set_ylabel(paras[1])
            ax.set_zlabel(vars[i])
        plt.show()

    def one_paras_analysis(self,para_vars,n_div=10,var_vars=None):
        # para_vars中的第一个用于遍历
        paras = []
        vars = []
        if var_vars == None:
            for key in self.items_setting.keys():
                if key in para_vars:
                    self.items_setting[key].type = 'Param'
                    if key in para_vars[0:1]:
                        paras.append(key)
                else:
                    self.items_setting[key].type = 'Var'
                    vars.append(key)
        else:
            for key in self.items_setting.keys():
                if key in para_vars:
                    self.items_setting[key].type = 'Param'
                    if key in para_vars[0:1]:
                        paras.append(key)
                elif key in var_vars:
                    self.items_setting[key].type = 'Var'
                    paras.append(key)
                else:
                    self.items_setting[key].type = 'Var'
        if len(para_vars) < 1:
            raise Exception("one_paras_analysis need at least 1 para.")
        if len(para_vars) != self.n_para:
            raise Exception("The number of given parameters is inconsistent with the dof.")
        iter_domain = []
        for para in paras:
            iter_domain.append([self.items_setting[para].domain[0], self.items_setting[para].domain[1]])
        iter_num = [n_div for k in range(len(paras))]
        para_samples = []
        var_samples = []
        iter = multi_variable_iter.iter_grid(iter_domain, iter_num)
        for sample in iter:
            self.items_setting[paras[0]].init_value = sample
            self.instancialize(para_vars)
            solution = self.solve()
            if solution != -1:
                result = []
                for j in range(len(vars)):
                    result.append(solution[vars[j]])
                var_samples.append(result)
                para_samples.append(sample)
        rows = math.ceil(len(vars) / 2)
        x = para_samples
        var_samples = np.array(var_samples)
        fig = plt.figure()
        for i in range(len(vars)):
            y = var_samples[:, i]
            ax = fig.add_subplot(rows * 100 + 20 + i + 1)
            ax.plot(x,y,linestyle='-')
            ax.set_xlabel(paras[0])
            ax.set_ylabel(vars[i])
        plt.show()

    def get_charasteristic(self,para_vars,n_sample=100):
        paras = []
        vars = []
        infeasible_points = np.array([])
        for key in self.items_setting.keys():
            if key in para_vars:
                self.items_setting[key].type = 'Param'
                paras.append(key)
            else:
                self.items_setting[key].type = 'Var'
                vars.append(key)
        samples = np.random.uniform(0, 1, size=(n_sample, self.n_para))
        result = np.zeros(shape=(n_sample, len(vars)))
        result_items = 0
        for i in range(self.n_para):
            offset = (self.items_setting[paras[i]].domain[0] + self.items_setting[paras[i]].domain[1]) / 2
            gain = -self.items_setting[paras[i]].domain[0] + self.items_setting[paras[i]].domain[1]
            for j in range(n_sample):
                samples[j, i] = (samples[j, i] - 0.5) * gain + offset
        feasible_samples = []
        for i in range(n_sample):
            for j in range(self.n_para):
                self.items_setting[paras[j]].init_value = samples[i,j]
            self.instancialize(para_vars)
            solution = self.solve()
            if solution != -1:
                for j in range(len(vars)):
                    result[result_items, j] = solution[vars[j]]
                result_items+=1
                feasible_samples.append(samples[i,:])
            else:
                infeasible_points.append(samples[i,:])
        result = result[0:result_items,:]
        A=[]
        b=[]
        for j in range(len(vars)):
            reg = LinearRegression().fit(feasible_samples, result[:,j])
            A.append(reg.coef_)
            b.append(reg.intercept_)
        return A,b,infeasible_points
