'''What to do with missing values?'''
"""You can use approximation instead of dropping responses/ items with missing values"""

import numpy as np
import pandas as pd

from pandas import Series, DataFrame

'''Finding out which data is missing'''
missing = np.nan

S_obj = Series(['row1', 'row2', missing, 'row4', 'row5', 'row6', missing, 'row8'])
'''prints current series'''
print(S_obj)

'''Prints True for missing entries, otherwise will be False'''
print(S_obj.isnull())

'''Filling in Missing Values'''

"""Create and print DF full of random values"""
np.random.seed(25)
DF_obj = DataFrame(np.random.randn(36).reshape(6,6))
print(DF_obj)
'''Changed values in column 0 and in the specifed rows to missing'''
DF_obj.loc[3:5, 0] = missing
'''Changed values in column 5 and in the specifed rows to missing'''
DF_obj.loc[1:4, 5] = missing
'''shows changes'''
print(DF_obj)

'''fillna method'''
"""fills in missing values with a user specified value"""

'''Replaces and prints missing values as 0'''
Filled_DF = DF_obj.fillna(0)
print(Filled_DF)

'''Uses a dictionary to specify the values of each column when filling in the dataset'''
Filled_DF = DF_obj.fillna({0: 0.1, 5: 1.25})
print(Filled_DF)

'''Fills null values with the last non null value'''
Fill_DF = DF_obj.fillna(method='ffill')
print(Fill_DF)

'''Counting Missing Values'''
"""Counting is useful to help figure out which variables are the most problematic"""

print(DF_obj)
'''Displays the  count of null values in each column'''
print(DF_obj.isnull().sum())

'''Filtering Missing Values'''
"""Gets rid of rows with missing values and prints the rows without any missing values """
DF_no_NaN = DF_obj.dropna()
print(DF_no_NaN)

'''Drops the columns with any missing values, not the row'''
DF_no_NaN = DF_obj.dropna(axis=1)
print(DF_no_NaN)