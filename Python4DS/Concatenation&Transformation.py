'''File describes Concatenation and Transformation of data'''

import numpy as np
import pandas as pd

from pandas import Series, DataFrame

'''generate a DF with values from 0-35'''
df_obj = pd.DataFrame(np.arange(36).reshape(6,6))
print(df_obj)
'''creates second DF with values from 0-15'''
"""Allows use to concatenate these DFs"""
df_obj2 = pd.DataFrame(np.arange(15).reshape(5,3))
print(df_obj2)

'''axis = 1, tells python that we want to concatenate by columns, by row index values'''
print(pd.concat([df_obj, df_obj2], axis = 1))
'''to flip it we can exclude the axis portion of the command'''
print(pd.concat([df_obj, df_obj2]))

"""^^^^These leave some spots as NaN as the tables were not of equal size"""

'''Transforming Data'''
"""Drops unwanted data from rows indexed at 0 and 2"""
print(df_obj.drop([0,2]))

'''Can change this to columns with the addition of axis = 1 after the closing ] '''

"""Adding Data"""
'''Creates new series to be added to the DF'''
s_obj = Series(np.arange(6))
s_obj.name = "added_variable"
print(s_obj)

'''Joining the 2 obj'''
"""Join Method"""
variable_added= DataFrame.join(df_obj, s_obj)
print(variable_added)

"""Append Method"""
added_datatable = variable_added.append(variable_added, ignore_index = False)
print(added_datatable)