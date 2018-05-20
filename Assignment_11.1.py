# -*- coding: utf-8 -*-
"""
Created on Thu May 17 22:07:07 2018

@author: singh.shivam
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
 
titanic = pd.read_csv('titanic_original.csv')
M_f = titanic.groupby('sex').count()
# Data to plot
labels =M_f.index.values 
sizes = M_f['pclass']
colors = ['gold', 'yellowgreen']
explode = (0.1, 0)  # explode 1st slice
# Plot
plt.pie(sizes, explode=explode, labels=labels, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
 
plt.axis('equal')
plt.title('Distribution of Male and Female')
plt.show()


titanic.age = titanic.age.fillna(titanic.age.mean())
titanic.fare = titanic.fare.fillna(titanic.fare.mean())
titanic.sex = titanic.sex.fillna('female')
#print(titanic.isnull().sum())

# Create data

x = titanic['age']
y = titanic['fare']
colors = np.where(titanic.sex =='female','gold','yellowgreen')
# Plot
plt.scatter(x, y, c=colors, alpha=0.6)
plt.title('Scatter plot b/w Age And Fare with Color distribution uisng sex')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()


