# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 20:13:45 2023

@author: hitan
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data = {'year': [2010,2011,2012,2013,2012,2013,2011,2016],
        'team' : ['Bears','Bears','Bears','Packers',
                  'Packers','Lions','Lions','Lions'],
        'wins' : [11,8,10,15,11,6,10,4],
        'losses' : [5,8,6,1,5,10,6,12]
        }
# dataframe is pandas 2D data structure similar to excel sheets
football = pd.DataFrame(data,
                        columns=['year','team','wins','losses'])
print(football.head())
print("---------")
print(football["year"])
x = football["year"]
y = football["wins"]
# set x limits
plt.xlim(2010,2013)
#set x ticks
plt.xticks(np.linspace(2010,2013,4,endpoint=True))
#np.linespace(startnum,endnum,number of values to be generated)
plt.ylim(2,16)
plt.yticks(np.linspace(2,16,8, endpoint=True))
plt.bar(x,y)
plt.show()