# -*- coding: utf-8 -*-
"""
Created on Fri Jul 28 12:30:30 2023

@author: hitan
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("C:/Users/hitan/OneDrive/Desktop/downloads/website.csv")
data.head()

print(data.shape)

data.info()

data.describe()

