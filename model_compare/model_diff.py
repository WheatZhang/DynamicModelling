#!/usr/bin/env python
#-*- coding:utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import random

def model1(x):
    if not isinstance(x, np.ndarray):
        x = np.array(x)
    return np.sin(x)

def model2(x):
    if not isinstance(x, np.ndarray):
        x = np.array(x)
    return x

class RealStaticModel(object):
    def __init__(self, model, n_x, n_y, domain, y_range):
        self.model = model
        self.n_x = n_x
        self.n_y = n_y
        if not isinstance(domain, np.ndarray):
            domain = np.array(domain)
        if not isinstance(y_range, np.ndarray):
            y_range = np.array(y_range)
        if domain.ndim == 1:
            if domain.shape[0]!=2:
                raise Exception("The shape of domain is not correct.")
            if domain[0]>= domain[1]:
                raise Exception("The value of domain is not correct.")
            new_domain = np.zeros(shape=(n_x,2))
            for i in range(n_x):
                new_domain[i,:] = domain
            self.domain = new_domain
        elif domain.ndim == 2:
            if domain.shape[1] != 2 or domain.shape[0] != n_x:
                raise Exception("The shape of domain is not correct.")
            for i in range(n_x):
                if domain[i,0]>= domain[i,1]:
                    raise Exception("The value of domain is not correct.")
            self.domain = domain
        else:
            raise Exception("The shape of domain is not correct.")
        if y_range.ndim == 1:
            if y_range.shape[0]!=2:
                raise Exception("The shape of y_range is not correct.")
            if y_range[0]>= y_range[1]:
                raise Exception("The value of y_range is not correct.")
            new_y_range = np.zeros(shape=(n_y,2))
            for i in range(n_y):
                new_y_range[i,:] = y_range
            self.y_range = new_y_range
        elif y_range.ndim == 2:
            if y_range.shape[1] != 2 or y_range.shape[0] != n_y:
                raise Exception("The shape of y_range is not correct.")
            for i in range(n_y):
                if y_range[i,0]>= y_range[i,1]:
                    raise Exception("The value of y_range is not correct.")
            self.y_range = y_range
        else:
            raise Exception("The shape of y_range is not correct.")

    def simulate(self, n_sample = 10):
        samples = np.random.uniform(0,1,size=(n_sample, self.n_x))
        for i in range(self.n_x):
            offset = (self.domain[i,0]+self.domain[i,1])/2
            gain = -self.domain[i,0]+self.domain[i,1]
            for j in range(n_sample):
                samples[j,i] = (samples[j,i]-0.5)*gain+offset
        result = np.zeros(shape=(n_sample, self.n_y))
        for i in range(n_sample):
            try:
                result[i,:] = self.model(samples[i,:])
            except Exception:
                for j in range(self.n_y):
                    result[i,j] = (self.y_range[j,0]+self.y_range[j,1])/2
        for i in range(self.n_y):
            for j in range(n_sample):
                if result[j,i] < self.y_range[i,0]:
                    result[j, i] = self.y_range[i, 0]
                elif result[j,i] > self.y_range[i,1]:
                    result[j, i] = self.y_range[i, 1]
        return samples,result

    def compare_to(self, model2, n_sample = 10):
        if self.n_x != model2.n_x or self.n_y != model2.n_y:
            raise Exception("Two models have different size.")
        for i in range(self.n_x):
            if self.domain[i,0] != model2.domain[i,0] or self.domain[i,1] != model2.domain[i,1]:
                print("Warning: the two models have different domain")
        samples = np.random.uniform(0,1,size=(n_sample, self.n_x))
        for i in range(self.n_x):
            offset = (self.domain[i,0]+self.domain[i,1])/2
            gain = -self.domain[i,0]+self.domain[i,1]
            for j in range(n_sample):
                samples[j,i] = (samples[j,i]-0.5)*gain+offset
        comp_value = 0
        range_size = 1
        for i in range(self.n_y):
            range_size *= self.y_range[i,1]-self.y_range[i,0]
        for i in range(n_sample):
            result = np.zeros(shape=(self.n_y,))
            result_model2 = np.zeros(shape=(self.n_y,))
            try:
                result = self.model(samples[i,:])
            except Exception:
                for j in range(self.n_y):
                    result[j] = (self.y_range[j,0]+self.y_range[j,1])/2
                for j in range(self.n_y):
                    if result[j] < self.y_range[i,0]:
                        result[j] = self.y_range[i, 0]
                    elif result[j] > self.y_range[i,1]:
                        result[j] = self.y_range[i, 1]
            try:
                result_model2 = model2.model(samples[i, :])
            except Exception:
                for j in range(model2.n_y):
                    result_model2[j] = (model2.y_range[j, 0] + model2.y_range[j, 1]) / 2
                for j in range(model2.n_y):
                    if result_model2[j] < model2.y_range[i, 0]:
                        result_model2[j] = model2.y_range[i, 0]
                    elif result_model2[j] > model2.y_range[i, 1]:
                        result_model2[j] = model2.y_range[i, 1]
            error = 1
            for j in range(self.n_y):
                error *= result[j] - result_model2[j]
            error = np.abs(error)
            score = np.log(range_size/error)
            if score > 10:
                comp_value+=10
            else:
                comp_value+=score
        return comp_value/n_sample

model_a = RealStaticModel(model1, 2,2,[-10,10],[-5,5])
model_b = RealStaticModel(model2, 2,2,[-10,10],[-5,5])
samples,result = model_a.simulate(n_sample = 50)
samples2,result2 = model_b.simulate(n_sample = 50)
plt.plot(samples[:,1],result[:,1],'.')
plt.plot(samples2[:,1],result2[:,1],'.')
plt.show()
print(model_a.compare_to(model_b, n_sample = 50))