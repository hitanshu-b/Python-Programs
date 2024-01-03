# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 16:08:08 2023

@author: hitan
"""

import matplotlib.pyplot as plt

x = [1,2,3]
y = [5,7,4]
x1 = [1,2,4]
y1 = [10,13,14]
plt.plot(x,y,label="First Line")
plt.plot(x1,y1,label="Second Line")
plt.xlabel('Plot Number')
plt.ylabel('Important Var')
plt.legend()
# plt.grid()
plt.title('First Line Graph using Matplotlib')
plt.show()

#Piechart

import matplotlib.pyplot as plt

slices = [7,8,6,11,7]
activities = ['excercise','sleeping','working','eating','playing']
cols = ['g','c','m','r','k']

plt.pie(slices,labels=activities,colors=cols,startangle=90,
        shadow=True, explode=(0.2,0,0.1,0,0))
plt.title('Piechart')
plt.show()

# Bar graph

import pylab as plt

DayOfWeekOfCall = [1,2,3]
DispatchesOnThisWeekday = [77,32,42]

LABELS= ["Monday","Tuesday","Wednesday"]

plt.bar(DayOfWeekOfCall,DispatchesOnThisWeekday,align='center')
plt.xticks(DayOfWeekOfCall, LABELS,rotation="45")
plt.show()

# stack plot graph

import matplotlib.pyplot as plt

days = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,7,2]
playing = [8,5,7,8,13]

# in stackplot we cannot give labels, so to create legend use following.

plt.plot([],[], color='m', label='sleeping',linewidth=5)
plt.plot([],[], color='c', label='Eating',linewidth=5)
plt.plot([],[], color='r', label='Working',linewidth=5)
plt.plot([],[], color='b', label='Playing',linewidth=5)

plt.stackplot(days,sleeping,eating,working,playing,colors=['m','c','r','b'])

plt.xlabel('plot number')
plt.ylabel('Important var')
plt.legend(loc="upper left")
plt.title('StackPlot Demo')
plt.show()


# Scatter Plot

import matplotlib.pyplot as plt

enrollment = [10,100,70,34,56,110,124,145,120,11,45,35,4,7]
# classroom =[x for x in range(len(enrollment))]
students = [0,10,20,30,40,50,60,70,80,90,100,110,120,130]

plt.scatter(enrollment, students, label="Scatter Plot",color='green',marker=5)

plt.xlabel('plot number')
plt.ylabel('Important var')
plt.legend()
plt.title("Scatter plot")
plt.show()