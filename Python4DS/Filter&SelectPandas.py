'''Pandas is good for fast data cleaning, preparation,
and analysis + easy for data visualization and machine learning'''

"""Arrays and matrices are called series and dataframes in pandas"""

import numpy as np
import pandas as pd

from pandas import Series, DataFrame
'''creates a sequential series from 0-7'''
S_obj = Series(np.arrange(8), index=['row1', 'row2', 'row3', 'row4', 'row5', 'row6', 'row7', 'row8'])
print(S_obj)
