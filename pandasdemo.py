# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 13:14:06 2023

@author: hitan
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

s = pd.Series(np.random.randn(5), index=['a','b','c','d','e'])
# print(s)
# # print(s[:4])
# # s = pd.Series(np.random.randint(5,size=5),index=['a','b','c','d','e'])
# # print(s)
# # print(s.index)
# print(s>s.median())
# print(s.get('f'))

mydata= pd.read_table("http://bit.ly/chiporders")
# if we need names of columns
print(mydata.columns)
# to check how many rows/columns are there
print(mydata.shape)
# to check first few rows
print(mydata.head())
# to check last five rows
print(mydata.tail())
# to check information about the dataframe
print(mydata.info())
# to get required calculations of statsitical functions like mean, median, mode
print(mydata.describe())
# to get data of a particular row by number
df= mydata.iloc[2:10,1:4]
# to get data of a particular row/column by name eg:dataframe
df1 = mydata.loc[2:10,["quantity","item_name"]]
# eg of data series
df2 = mydata.loc[2:10,"quantity"]
# unique fucntion works on data series
print(mydata["item_name"].unique())
#correlation
mydata.corr()
mydata["len_name"] = mydata["item_name"].map(lambda x:len(x))
def myfunction(val):
    return len(val)*10
def convertint(val):
    return float(val.replace("$",""))
mydata["mycnt"]=mydata["item_name"].apply(myfunction)
mydata["myprice"]=mydata["item_price"].apply(convertint)

mymoviedata = pd.read_table("http://bit.ly/movieusers",sep="|",header=None)
print(mymoviedata.columns)
# to assign names to the unnamed columns
mymoviedata.columns["id","age","gender","profession","views"]
print(mymoviedata.shape)
print(mymoviedata.head(8))
print(mymoviedata.tail())
print(mymoviedata["age"].mean())
