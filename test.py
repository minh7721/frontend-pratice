from __future__ import division, print_function, unicode_literals
import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd

import tkinter as tk
from tkinter import *
from tkinter import messagebox

master=tk.Tk()
master.title("Dự đoán giá Biệt thự")
tk.Label(master, text="Nhập các thông tin dưới đây", fg='blue').grid (column=0, row=0)

tk.Label (master, text="Nhập Số Tầng(tầng) :", fg='blue').grid (column=0, row=1)
s1 = Entry(master,width=70)
s1.grid(column=1, row=1)
tk.Label (master, text="Nhập Diện Tích(m2) :", fg='blue').grid (column=0, row=2)
s2 = Entry(master,width=70)
s2.grid(column=1, row=2)
tk.Label (master, text="Nhập Số Mét Mặt Tiền(m) :", fg='blue').grid (column=0, row=3)
s3 = Entry(master,width=70)
s3.grid(column=1, row=3)
tk.Label (master, text="Nhập Giá Thực Tế (đ):", fg='blue').grid (column=0, row=4)
s4 = Entry(master,width=70)
s4.grid(column=1, row=4)

##### truyền dữ liệu ######
b_x= 'DuLieu.txt'
b_y= 'Gia.txt'
data=pd.read_csv(b_x,sep='\t')
label=pd.read_csv(b_y,sep='\t')
print(type(data))
print("-----------------")
X = data.values
print(X)
print("-----------------")
print(label)
print("-----------------")
X = data.values
Y = label.values
print(X.shape)
print("-----------------")
print(Y.shape)
print("-----------------")

one = np.ones((X.shape[0], 1))
Xbar = np.concatenate((one, X), axis = 1)

A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, Y)
w = np.dot(np.linalg.pinv(A), b)
print ('w=',w)
print("-----------------")

w_0 = w[0][0]
w_1 = w[1][0]
w_2 = w[2][0]
w_3 = w[3][0]

def predict():
	b1=float(s1.get())
	b2=float(s2.get())
	b3=float(s3.get())
	b4=float(s4.get())
	y_0 = w_0 + w_1 * b1 + w_2 * b2 + w_3 * b3
	e = (1/2)*1.0*(pow(b4 - y_0,2))
	messagebox.showinfo("Giá phần mềm: ",y_0)
	messagebox.showinfo("Sai số: ",e)

### Test dữ liệu ###
test_x= 'DuLieuTest.txt'
test_y= 'GiaDuLieuTest.txt'
data_test=pd.read_csv(test_x,sep='\t')
label_test=pd.read_csv(test_y,sep='\t')
X_test = data_test.values
Y_test = label_test.values
print(X_test.shape)
print("-----------------")
print("Dữ liệu test: ")
print(X_test)
print("-----------------")
print("Kết quả test: ")
print("-----------------")
for test in range(20):
        y_0 = w_0 + w_1 * X_test[test][0] + w_2 * X_test[test][1] + w_3 * X_test[test][2]
        print(str(test+1) + " : " + str(y_0))


print("Giá Thực Tế:")
for gia in range(20):
        print(str(gia+1) + " : " + str(Y_test[gia]))
tk.Button(master,  text='Enter', command=predict).grid(row=5, 
                                                       column=1, 
                                                       sticky=tk.W, 
                                                       pady=5)

#master.mainloop()
#x1 = float(input("Nhập số Tầng: "))
#x2 = float(input("nhập diện tích: "))
#x3 = float(input("Nhập số mặt tiền: "))

#giadudoan =  w_3*x3 + w_2*x2 + w_1*x1 + w_0
#print(  u'giabietthududoan: %.2f' %(giadudoan))
