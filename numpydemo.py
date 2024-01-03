# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 17:16:32 2023

@author: hitan
"""

import numpy as np

# a = np.array([1,2,3,4])
# b = np.array([(1.2,5,3),(4,5,6)])
# c = np.array([[1,2],[3,4]],dtype=complex)
# print(a.ndim)
# print(b.ndim)
# print(a.dtype)
# print(b.itemsize)
np.zeros((3,4))
# d = np.ones( (2,3,4), dtype=np.int16)
# print(d)
e = np.arange(12).reshape(4,3)
print(e)
f = np.arange(24).reshape(2,3,4)
print(f)

arr = np.array(50)
print(arr.ndim)

d = np.arange(4,27,2).reshape(4,3)
print(d)
print(d[1:3,1:3])

# to display 1st row and 1st 2 cloumns
print(d[1,:2])

# barr = b.astype("i")
# print(barr.dtype)

# string array
sarr = np.array(["python","java","perl"])
print(sarr.dtype)

a = np.array([20,30,40,60])
b = np.arange(4)
print(b)
c = a - b
print(c)
print(b**2)
print(10*np.sin(a))

# concatenate
concarr = np.concatenate((b,c))
print(concarr)
print(np.stack((b,c)))
print(np.hstack((b,c)))
print(np.vstack((b,c)))

x = np.eye(3,4,k=1)
print("\nMatrix A:\n",x)

s
