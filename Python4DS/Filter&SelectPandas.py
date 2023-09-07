'''Pandas is good for fast data cleaning, preparation,
and analysis + easy for data visualization and machine learning'''

"""Arrays and matrices are called series and dataframes in pandas"""

import numpy as np
import pandas as pd

from pandas import Series, DataFrame
'''creates a sequential series from 0-7'''
S_obj = Series(np.arange(8), index=['row1', 'row2', 'row3', 'row4', 'row5', 'row6', 'row7', 'row8'])
'''selects and prints all labels'''
print(S_obj)
'''selects and prints all labels with this index'''
print(S_obj['row7'])
'''selects and prints all labels with this int index'''
print(S_obj[[0,7]])

'''generating random numbers with numpy for Data Frame'''
np.random.seed(25)
DF_obj = DataFrame(np.random.rand(36).reshape((6,6)),
                   index=['row1', 'row2', 'row3', 'row4', 'row5', 'row6'],
                   columns=['column1', 'column2', 'column3', 'column4', 'column5', 'column6'])
print(DF_obj)

'''gets values at rows 2 and 5 and columns 2 and 5 (2x2 matrix)'''
print(DF_obj.loc[['row2', 'row5'], ['column2', 'column5']])

'''Data Slicing'''
"""Slicing returns a slice of several values from a dataset and is an inclusive operation
getting all values in between selected start and finish"""

'''prints values of rows 3-7'''
print(S_obj['row3':'row7'])

'''Comparing with Scalars allows you to see how a dataset compares to a specified boolean statement'''

'''Shows which values are less than .2'''
print(DF_obj < .2)

'''Filtering with Scalars'''
"""Returns only the records that follow the specified boolean statement"""

'''prints out all the values from S_obj > 4'''
print(S_obj[S_obj > 4])


'''Setting values with scalars'''
"""Select all values in the specifed index and change their value to a specified scalar"""

S_obj['row1'] = 9
'''Jupyter notebooks allows for multiple updates at once, while VScode requires multiple without
an exception being thrown'''
S_obj['row4'] = 2000
print(S_obj)