# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 14:24:27 2023

@author: hitan
"""

# modules we'll use
import pandas as pd
import numpy as np

# read in all our data
nfl_data = pd.read_csv("../input/nflplaybyplay2009to2016/NFL Play by Play 2009-2017 (v4).csv")

# set seed for reproducibility
np.random.seed(0) 

# look at the first five rows of the nfl_data file. 
# I can see a handful of missing data already!
nfl_data.head()

# get the number of missing data points per column
missing_values_count = nfl_data.isnull().sum()

# look at the # of missing points in the first ten columns
missing_values_count[0:10]

# how many total missing values do we have?
total_cells = np.product(nfl_data.shape)
total_missing = missing_values_count.sum()

# percent of data that is missing
percent_missing = (total_missing/total_cells) * 100
print(percent_missing)

# look at the # of missing points in the first ten columns
missing_values_count[0:10]

# remove all the rows that contain a missing value
nfl_data.dropna()