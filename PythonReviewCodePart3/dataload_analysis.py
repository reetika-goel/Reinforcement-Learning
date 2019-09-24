# -*- coding: utf-8 -*-
"""
Created on Wed Sep 12 08:44:37 2018

@author: jahan
"""


import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import scatter_matrix
from pandas import set_option
from pandas import read_csv


filename = 'pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = read_csv(filename, names = names)

# save features as pandas dataframe for stepwise feature selection
X1 = data.drop(data.columns[8], axis = 1)
Y1 = data.drop(data.columns[0:8], axis = 1)
# separate features and response into two different arrays
array = data.values
X = array[:,0:8]
Y = array[:,8]
# First perform exploratory data analysis using correlation and scatter plot
# look at the first 20 rows of data
peek = data.head(20)
print(peek)

# descriptive statistics: mean, max, min, count, 25 percentile, 50 percentile, 75 percentile
set_option('display.width', 100)
set_option('precision', 1)
description = data.describe()
print(description)

# we look at the distribution of data and its descriptive statistics
data.hist()
plt.show()


# correlation heat map, pay attention to correlation between all predicators/features and each predictor and the output
plt.figure() # new plot
corMat = data.corr(method='pearson')
print(corMat)
# plot correlation matrix as a heat map
sns.heatmap(corMat, square=True)
plt.yticks(rotation=0)
plt.xticks(rotation=90)
plt.title("CORELATION MATTRIX USING HEAT MAP")
plt.show()

# scatter plot of all data
scatter_matrix(data)
plt.show()
