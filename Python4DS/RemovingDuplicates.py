"""Can cause records of a single entity being counted as multiple seperate entities"""
'''Important to remove them to not skew the data'''
import numpy as np
import pandas as pd

from pandas import Series, DataFrame

df_obj = DataFrame({'column1': [1,1,2,2,3,3,3],
                    'column2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
                    'column3': ['A', 'A', 'B', 'B', 'C', 'C', 'C']})
'''to display current matrix'''
print(df_obj)

'''Checks if a entry is a duplicate or unique'''
"""First row counted as unique, each subsequent copy is a duplicate"""
print(df_obj.duplicated())

'''Drops duplicates and displays only unique elements'''
print(df_obj.drop_duplicates())

'''Updating data frame (not best method)'''
df_obj = DataFrame({'column1': [1,1,2,2,3,3,3],
                    'column2': ['a', 'a', 'b', 'b', 'c', 'c', 'c'],
                    'column3': ['A', 'A', 'B', 'B', 'C', 'D', 'C']})

'''prints new DF'''
print(df_obj)
"""drops entries with duplicates in column3, and then prints the final result"""
'''Doesn't care about duplicate in column2 or column1'''
print(df_obj.drop_duplicates(['column3']))