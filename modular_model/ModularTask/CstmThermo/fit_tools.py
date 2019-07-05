#!/usr/bin/env python
#-*- coding:utf-8 -*-
from scipy.optimize import minimize
import numpy as np

def binary_cubic_polyfit(x,y,z,filename,funcname,x_name="crude_x", y_name = "crude_y"):
    func_file = open(filename+".py", 'a+')
    func_file.write("def "+funcname+"("+x_name+","+y_name+"):\n")
    def fit(x,y, params):
        z = np.zeros(shape=x.shape)
        for i in range(z.size):
            xv=np.array([1,x[i],x[i]*x[i],x[i]*x[i]*x[i]])
            yv = np.array([1, y[i], y[i] * y[i], y[i] * y[i] * y[i]])
            for j in range(4):
                for k in range(4):
                    z[i]+=xv[j]*yv[k]*params[j*4+k]
        return z
    def cost_function(params, x, y, z):
        return np.linalg.norm(z - fit(x,y, params))
    x_min = np.min(x)
    x_max = np.max(x)
    y_min = np.min(y)
    y_max = np.max(y)
    z_min = np.min(z)
    z_max = np.max(z)
    x = (x - x_min) / (x_max - x_min)
    y = (y - y_min) / (y_max - y_min)
    z = (z - z_min) / (z_max - z_min)
    func_file.write("\tx = ("+x_name+"-%f)/%f\n"%(x_min,x_max-x_min))
    func_file.write("\ty = ("+y_name+"-%f)/%f\n" % (y_min, y_max - y_min))
    func_file.write("\tx2 = x*x\n")
    func_file.write("\tx3 = x*x2\n")
    func_file.write("\ty2 = y*y\n")
    func_file.write("\ty3 = y*y2\n")
    func_file.write("\txy = x*y\n")
    func_file.write("\tx2y = x2*y\n")
    func_file.write("\txy2 = x*y2\n")
    func_file.write("\tx3y = x3*y\n")
    func_file.write("\tx2y2 = x2*y2\n")
    func_file.write("\txy3 = x*y3\n")
    func_file.write("\tx3y2 = x3*y2\n")
    func_file.write("\tx2y3 = x2*y3\n")
    func_file.write("\tx3y3 = x3*y3\n")
    x0 = np.zeros(shape=(16,))
    output = minimize(cost_function, x0, args=(x, y, z))
    func_file.write("\tz = %f+\\\n" % output.x[0])
    func_file.write("\t    y*%f+\\\n" % output.x[1])
    func_file.write("\t    y2*%f+\\\n" % output.x[2])
    func_file.write("\t    y3*%f+\\\n" % output.x[3])
    func_file.write("\t    x*%f+\\\n" % output.x[4])
    func_file.write("\t    xy*%f+\\\n" % output.x[5])
    func_file.write("\t    xy2*%f+\\\n" % output.x[6])
    func_file.write("\t    xy3*%f+\\\n" % output.x[7])
    func_file.write("\t    x2*%f+\\\n" % output.x[8])
    func_file.write("\t    x2y*%f+\\\n" % output.x[9])
    func_file.write("\t    x2y2*%f+\\\n" % output.x[10])
    func_file.write("\t    x2y3*%f+\\\n" % output.x[11])
    func_file.write("\t    x3*%f+\\\n" % output.x[12])
    func_file.write("\t    x3y*%f+\\\n" % output.x[13])
    func_file.write("\t    x3y2*%f+\\\n" % output.x[14])
    func_file.write("\t    x3y3*%f\n" % output.x[15])
    func_file.write("\treturn z*%f+%f\n" % (z_max - z_min, z_min))
    func_file.close()
    # print(output.x)
    func_file = open(funcname + "_mod.txt", 'w')
    func_file.write("BinaryBicubic\n")
    func_file.write(funcname + "\n")
    func_file.write(x_name + "\n")
    func_file.write(y_name + "\n")
    func_file.write(str(x_min)+"\n")
    func_file.write(str(x_max)+"\n")
    func_file.write(str(y_min)+"\n")
    func_file.write(str(y_max)+"\n")
    func_file.write(str(z_min)+"\n")
    func_file.write(str(z_max)+"\n")
    for i in output.x:
        func_file.write(str(i)+"\n")
    func_file.close()

def binary_4th_polyfit(x,y,z,filename,funcname,x_name="crude_x", y_name = "crude_y"):
    func_file = open(filename+".py", 'a+')
    func_file.write("def " + funcname + "(" + x_name + "," + y_name + "):\n")
    def fit(x,y, params):
        z = np.zeros(shape=x.shape)
        for i in range(z.shape[0]):
            z[i]=np.array([1,x[i],y[i],\
                           x[i]*x[i],x[i]*y[i],y[i]*y[i],\
                           x[i]*x[i]*x[i],x[i]*x[i]*y[i],x[i]*y[i]*y[i],y[i]*y[i]*y[i],\
                           x[i]*x[i]*x[i]*x[i],x[i]*x[i]*x[i]*y[i],x[i]*x[i]*y[i]*y[i],x[i]*y[i]*y[i]*y[i],y[i]*y[i]*y[i]*y[i]]).dot(params)
        return z
    def cost_function(params, x, y, z):
        return np.linalg.norm(z - fit(x,y, params))
    x_min = np.min(x)
    x_max = np.max(x)
    y_min = np.min(y)
    y_max = np.max(y)
    z_min = np.min(z)
    z_max = np.max(z)
    x = (x - x_min) / (x_max - x_min)
    y = (y - y_min) / (y_max - y_min)
    z = (z - z_min) / (z_max - z_min)
    func_file.write("\tx = (" + x_name + "-%f)/%f\n" % (x_min, x_max - x_min))
    func_file.write("\ty = (" + y_name + "-%f)/%f\n" % (y_min, y_max - y_min))
    func_file.write("\tx2 = x*x\n")
    func_file.write("\tx3 = x*x2\n")
    func_file.write("\tx4 = x*x3\n")
    func_file.write("\ty2 = y*y\n")
    func_file.write("\ty3 = y*y2\n")
    func_file.write("\ty4 = y*y3\n")
    func_file.write("\txy = x*y\n")
    func_file.write("\tx2y = x2*y\n")
    func_file.write("\txy2 = x*y2\n")
    func_file.write("\tx3y = x3*y\n")
    func_file.write("\tx2y2 = x2*y2\n")
    func_file.write("\txy3 = x*y3\n")
    x0 = np.zeros(shape=(15,))
    output = minimize(cost_function, x0, args=(x, y, z))
    func_file.write("\tz = %f+\\\n" % output.x[0])
    func_file.write("\t    x*%f+\\\n" % output.x[1])
    func_file.write("\t    y*%f+\\\n" % output.x[2])
    func_file.write("\t    x2*%f+\\\n" % output.x[3])
    func_file.write("\t    xy*%f+\\\n" % output.x[4])
    func_file.write("\t    y2*%f+\\\n" % output.x[5])
    func_file.write("\t    x3*%f+\\\n" % output.x[6])
    func_file.write("\t    x2y*%f+\\\n" % output.x[7])
    func_file.write("\t    xy2*%f+\\\n" % output.x[8])
    func_file.write("\t    y3*%f+\\\n" % output.x[9])
    func_file.write("\t    x4*%f+\\\n" % output.x[10])
    func_file.write("\t    x3y*%f+\\\n" % output.x[11])
    func_file.write("\t    x2y2*%f+\\\n" % output.x[12])
    func_file.write("\t    xy3*%f+\\\n" % output.x[13])
    func_file.write("\t    y4*%f\n" % output.x[14])
    func_file.write("\treturn z*%f+%f\n" % (z_max - z_min, z_min))
    func_file.close()
    # print(output.x)
    func_file = open(funcname + "_mod.txt", 'w')
    func_file.write("Binary4thOrder\n")
    func_file.write(funcname + "\n")
    func_file.write(x_name + "\n")
    func_file.write(y_name + "\n")
    func_file.write(str(x_min) + "\n")
    func_file.write(str(x_max) + "\n")
    func_file.write(str(y_min) + "\n")
    func_file.write(str(y_max) + "\n")
    func_file.write(str(z_min) + "\n")
    func_file.write(str(z_max) + "\n")
    for i in output.x:
        func_file.write(str(i) + "\n")
    func_file.close()

def derivative_cubic_polyfit(model_file, wrt_var):
    if wrt_var == "x":
        line_no = 0
        with open(model_file, 'r') as file_to_read:
            while True:
                lines = file_to_read.readline()  # 整行读取数据
                if not lines:
                    break
                else:
                    line_no += 1
                if line_no == 1:
                    if lines.strip() != "BinaryBicubic":
                        raise Exception("Model type is not correct.")
                elif line_no == 2:
                    z_name = lines.strip()
                elif line_no == 3:
                    x_name = lines.strip()
                elif line_no == 4:
                    y_name = lines.strip()
                elif line_no == 5:
                    x_min = float(lines.strip())
                elif line_no == 6:
                    x_max = float(lines.strip())
                elif line_no == 7:
                    y_min = float(lines.strip())
                elif line_no == 8:
                    y_max = float(lines.strip())
                elif line_no == 9:
                    z_min = float(lines.strip())
                elif line_no == 10:
                    z_max = float(lines.strip())
                elif line_no == 11:
                    coeff = []
                    coeff.append(float(lines.strip()))
                else:
                    coeff.append(float(lines.strip()))
        if len(coeff) != 16:
            raise Exception("Numbers of coefficients is not correct.")
        func_file = open(z_name + "_Dx.py", 'w')
        func_file.write("def " + z_name + "_Dx" + "(" + x_name + "," + y_name + "):\n")
        func_file.write("\tx = (" + x_name + "-%f)/%f\n" % (x_min, x_max - x_min))
        func_file.write("\ty = (" + y_name + "-%f)/%f\n" % (y_min, y_max - y_min))
        func_file.write("\tx2 = x*x\n")
        func_file.write("\ty2 = y*y\n")
        func_file.write("\ty3 = y*y2\n")
        func_file.write("\tx2dx = 2*x\n")
        func_file.write("\tx3dx = 3*x2\n")
        func_file.write("\txydx = y\n")
        func_file.write("\tx2ydx = 2*x*y\n")
        func_file.write("\txy2dx = y2\n")
        func_file.write("\tx3ydx = 3*x2*y\n")
        func_file.write("\tx2y2dx = 2*x*y2\n")
        func_file.write("\txy3dx = y3\n")
        func_file.write("\tx3y2dx = 3*x2*y2\n")
        func_file.write("\tx2y3dx = 2*x*y3\n")
        func_file.write("\tx3y3dx = 3*x2*y3\n")
        func_file.write("\tzdx = %f+\\\n" % coeff[4])
        func_file.write("\t    xydx*%f+\\\n" % coeff[5])
        func_file.write("\t    xy2dx*%f+\\\n" % coeff[6])
        func_file.write("\t    xy3dx*%f+\\\n" % coeff[7])
        func_file.write("\t    x2dx*%f+\\\n" % coeff[8])
        func_file.write("\t    x2ydx*%f+\\\n" % coeff[9])
        func_file.write("\t    x2y2dx*%f+\\\n" % coeff[10])
        func_file.write("\t    x2y3dx*%f+\\\n" % coeff[11])
        func_file.write("\t    x3dx*%f+\\\n" % coeff[12])
        func_file.write("\t    x3ydx*%f+\\\n" % coeff[13])
        func_file.write("\t    x3y2dx*%f+\\\n" % coeff[14])
        func_file.write("\t    x3y3dx*%f\n" % coeff[15])
        func_file.write("\treturn zdx*%f\n" % ((z_max - z_min) / (x_max - x_min)))
        func_file.close()
    elif wrt_var == "y":
        line_no = 0
        with open(model_file, 'r') as file_to_read:
            while True:
                lines = file_to_read.readline()  # 整行读取数据
                if not lines:
                    break
                else:
                    line_no += 1
                if line_no == 1:
                    if lines.strip() != "BinaryBicubic":
                        raise Exception("Model type is not correct.")
                elif line_no == 2:
                    z_name = lines.strip()
                elif line_no == 3:
                    x_name = lines.strip()
                elif line_no == 4:
                    y_name = lines.strip()
                elif line_no == 5:
                    x_min = float(lines.strip())
                elif line_no == 6:
                    x_max = float(lines.strip())
                elif line_no == 7:
                    y_min = float(lines.strip())
                elif line_no == 8:
                    y_max = float(lines.strip())
                elif line_no == 9:
                    z_min = float(lines.strip())
                elif line_no == 10:
                    z_max = float(lines.strip())
                elif line_no == 11:
                    coeff = []
                    coeff.append(float(lines.strip()))
                else:
                    coeff.append(float(lines.strip()))
        if len(coeff) != 16:
            raise Exception("Numbers of coefficients is not correct.")
        func_file = open(z_name + "_Dy.py", 'w')
        func_file.write("def " + z_name + "_Dy" + "(" + x_name + "," + y_name + "):\n")
        func_file.write("\tx = (" + x_name + "-%f)/%f\n" % (x_min, x_max - x_min))
        func_file.write("\ty = (" + y_name + "-%f)/%f\n" % (y_min, y_max - y_min))
        func_file.write("\ty2 = y*y\n")
        func_file.write("\tx2 = x*x\n")
        func_file.write("\tx3 = x*x2\n")
        func_file.write("\ty2dy = 2*y\n")
        func_file.write("\ty3dy = 3*y2\n")
        func_file.write("\tyxdy = x\n")
        func_file.write("\ty2xdy = 2*y*x\n")
        func_file.write("\tyx2dy = x2\n")
        func_file.write("\ty3xdy = 3*y2*x\n")
        func_file.write("\ty2x2dy = 2*y*x2\n")
        func_file.write("\tyx3dy = x3\n")
        func_file.write("\ty3x2dy = 3*y2*x2\n")
        func_file.write("\ty2x3dy = 2*y*x3\n")
        func_file.write("\ty3x3dy = 3*y2*x3\n")
        func_file.write("\tzdy = %f+\\\n" % coeff[1])
        func_file.write("\t    yxdy*%f+\\\n" % coeff[5])
        func_file.write("\t    yx2dy*%f+\\\n" % coeff[9])
        func_file.write("\t    yx3dy*%f+\\\n" % coeff[13])
        func_file.write("\t    y2dy*%f+\\\n" % coeff[2])
        func_file.write("\t    y2xdy*%f+\\\n" % coeff[6])
        func_file.write("\t    y2x2dy*%f+\\\n" % coeff[10])
        func_file.write("\t    y2x3dy*%f+\\\n" % coeff[14])
        func_file.write("\t    y3dy*%f+\\\n" % coeff[3])
        func_file.write("\t    y3xdy*%f+\\\n" % coeff[7])
        func_file.write("\t    y3x2dy*%f+\\\n" % coeff[11])
        func_file.write("\t    y3x3dy*%f\n" % coeff[15])
        func_file.write("\treturn zdy*%f\n" % ((z_max - z_min) / (y_max - y_min)))
        func_file.close()
    else:
        raise Exception("wrt_var must be x or y.")

def derivative_4th_polyfit(model_file, wrt_var):
    if wrt_var == "x":
        line_no = 0
        with open(model_file, 'r') as file_to_read:
            while True:
                lines = file_to_read.readline()  # 整行读取数据
                if not lines:
                    break
                else:
                    line_no += 1
                if line_no == 1:
                    if lines.strip() != "Binary4thOrder":
                        raise Exception("Model type is not correct.")
                elif line_no == 2:
                    z_name = lines.strip()
                elif line_no == 3:
                    x_name = lines.strip()
                elif line_no == 4:
                    y_name = lines.strip()
                elif line_no == 5:
                    x_min = float(lines.strip())
                elif line_no == 6:
                    x_max = float(lines.strip())
                elif line_no == 7:
                    y_min = float(lines.strip())
                elif line_no == 8:
                    y_max = float(lines.strip())
                elif line_no == 9:
                    z_min = float(lines.strip())
                elif line_no == 10:
                    z_max = float(lines.strip())
                elif line_no == 11:
                    coeff = []
                    coeff.append(float(lines.strip()))
                else:
                    coeff.append(float(lines.strip()))
        if len(coeff) != 15:
            raise Exception("Numbers of coefficients is not correct.")
        func_file = open(z_name + "_Dx.py", 'w')
        func_file.write("def " + z_name + "_Dx" + "(" + x_name + "," + y_name + "):\n")
        func_file.write("\tx = (" + x_name + "-%f)/%f\n" % (x_min, x_max - x_min))
        func_file.write("\ty = (" + y_name + "-%f)/%f\n" % (y_min, y_max - y_min))
        func_file.write("\tx2 = x*x\n")
        func_file.write("\tx3 = x*x2\n")
        func_file.write("\ty2 = y*y\n")
        func_file.write("\ty3 = y*y2\n")
        func_file.write("\tx2dx = 2*x\n")
        func_file.write("\tx3dx = 3*x2\n")
        func_file.write("\tx4dx = 4*x3\n")
        func_file.write("\txydx = y\n")
        func_file.write("\tx2ydx = 2*x*y\n")
        func_file.write("\txy2dx = y2\n")
        func_file.write("\tx3ydx = 3*x2*y\n")
        func_file.write("\tx2y2dx = 2*x*y2\n")
        func_file.write("\txy3dx = y3\n")
        func_file.write("\tzdx = %f+\\\n" % coeff[1])
        func_file.write("\t    x2dx*%f+\\\n" % coeff[3])
        func_file.write("\t    xydx*%f+\\\n" % coeff[4])
        func_file.write("\t    x3dx*%f+\\\n" % coeff[6])
        func_file.write("\t    x2ydx*%f+\\\n" % coeff[7])
        func_file.write("\t    xy2dx*%f+\\\n" % coeff[8])
        func_file.write("\t    x4dx*%f+\\\n" % coeff[10])
        func_file.write("\t    x3ydx*%f+\\\n" % coeff[11])
        func_file.write("\t    x2y2dx*%f+\\\n" % coeff[12])
        func_file.write("\t    xy3dx*%f\n" % coeff[13])
        func_file.write("\treturn zdx*%f\n" % ((z_max - z_min)/(x_max-x_min)))
        func_file.close()
    elif wrt_var == "y":
        line_no = 0
        with open(model_file, 'r') as file_to_read:
            while True:
                lines = file_to_read.readline()  # 整行读取数据
                if not lines:
                    break
                else:
                    line_no += 1
                if line_no == 1:
                    if lines.strip() != "Binary4thOrder":
                        raise Exception("Model type is not correct.")
                elif line_no == 2:
                    z_name = lines.strip()
                elif line_no == 3:
                    x_name = lines.strip()
                elif line_no == 4:
                    y_name = lines.strip()
                elif line_no == 5:
                    x_min = float(lines.strip())
                elif line_no == 6:
                    x_max = float(lines.strip())
                elif line_no == 7:
                    y_min = float(lines.strip())
                elif line_no == 8:
                    y_max = float(lines.strip())
                elif line_no == 9:
                    z_min = float(lines.strip())
                elif line_no == 10:
                    z_max = float(lines.strip())
                elif line_no == 11:
                    coeff = []
                    coeff.append(float(lines.strip()))
                else:
                    coeff.append(float(lines.strip()))
        if len(coeff) != 15:
            raise Exception("Numbers of coefficients is not correct.")
        func_file = open(z_name + "_Dy.py", 'w')
        func_file.write("def " + z_name + "_Dy" + "(" + x_name + "," + y_name + "):\n")
        func_file.write("\tx = (" + x_name + "-%f)/%f\n" % (x_min, x_max - x_min))
        func_file.write("\ty = (" + y_name + "-%f)/%f\n" % (y_min, y_max - y_min))
        func_file.write("\ty2 = y*y\n")
        func_file.write("\ty3 = y*y2\n")
        func_file.write("\tx2 = x*x\n")
        func_file.write("\tx3 = x*x2\n")
        func_file.write("\ty2dy = 2*y\n")
        func_file.write("\ty3dy = 3*y2\n")
        func_file.write("\ty4dy = 4*y3\n")
        func_file.write("\tyxdy = x\n")
        func_file.write("\ty2xdy = 2*y*x\n")
        func_file.write("\tyx2dy = x2\n")
        func_file.write("\ty3xdy = 3*y2*x\n")
        func_file.write("\ty2x2dy = 2*y*x2\n")
        func_file.write("\tyx3dy = x3\n")
        func_file.write("\tzdy = %f+\\\n" % coeff[2])
        func_file.write("\t    y2dy*%f+\\\n" % coeff[5])
        func_file.write("\t    yxdy*%f+\\\n" % coeff[4])
        func_file.write("\t    y3dy*%f+\\\n" % coeff[9])
        func_file.write("\t    y2xdy*%f+\\\n" % coeff[8])
        func_file.write("\t    yx2dy*%f+\\\n" % coeff[7])
        func_file.write("\t    y4dy*%f+\\\n" % coeff[14])
        func_file.write("\t    y3xdy*%f+\\\n" % coeff[13])
        func_file.write("\t    y2x2dy*%f+\\\n" % coeff[12])
        func_file.write("\t    yx3dy*%f\n" % coeff[11])
        func_file.write("\treturn zdy*%f\n" % ((z_max - z_min)/(y_max-y_min)))
        func_file.close()
    else:
        raise Exception("wrt_var must be x or y.")