# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 06:55:59 2018

@author: jahan
"""

import pandas as pd

# Pandas data series
purchase1 = pd.Series({'Name': 'Chris',
                        'Item Purchased' : 'Dog Food',
                        'Cost' : 22.50})
purchase2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased' : 'Kitty Litter',
                        'Cost' : 2.50})
purchase3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased' : 'Bird Seed',
                        'Cost' : 5.00})
# Make a dataframe out of dataSeries
df = pd.DataFrame([purchase1, purchase2, purchase3], index = ['Store1', 'Store1', 'Store2'])
# Display data head
df.head()
# display data by row tag
df.loc['Store2']
# get type
type(df.loc['Store2'])
# select row and column
df.loc['Store1', 'Cost']

# transpose dataframe
df1 = df.T
# Get cost as a row tag
df.T.loc['Cost']

df['Cost']
df.loc['Store1']['Cost']
# Retrieving Column Using Slicing

df.loc[:,['Name', 'Cost']]

# read a .csv file
df_olympic =pd.read_csv('olympic.csv', encoding='windows-1252')
