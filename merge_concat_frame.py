# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 13:09:18 2023

@author: hitan
"""

#import libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dummy_data1 = {
    'id': ["1","2","3","4","5"],
    'feature1': ["A","C","E","G","I"],
    'feature2': ["B","D","F","H","J"]}

df1 = pd.DataFrame(dummy_data1, columns=["id","feature1","feature2"])
df1

dummy_data2 = {
    'id': ["1","2","5","7","9"],
    'feature1' : ["K","M","O","Q","S"],
    'feature2' : ["L","N","P","R","T"]
    }

df2 = pd.DataFrame(dummy_data2,columns=['id','feature1','feature2'])
df2

df1['dept'] = 'sales'
df2['dept'] = 'purchase'
combined_fr = pd.concat([df1,df2],ignore_index=True)

dummy_data3 = {
    'id': ['1','2','3','4','5','7','8','9','10','11'],
    'feature3': [12,13,14,15,16,17,15,12,13,23]}
df3 = pd.DataFrame(dummy_data3,columns=['id','feature3'])
df3

df4 = pd.merge(df2,df3,on='id') #by default inner join
df5 = pd.merge(df2, df3,on='id',how='left') # we can write right, outer or inner
