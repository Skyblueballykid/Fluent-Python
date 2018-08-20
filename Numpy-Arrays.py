'''
Additional helpful Numpy examples from:
 https://towardsdatascience.com/a-hitchhiker-guide-to-python-numpy-arrays-9358de570121
'''


import numpy as np

# Numpy arrays are only used for HOMOGENOUS data:
numpy_arr = np.array([1,2,"Hello",3,"World"], dtype=int32) # throws an error

# Lists can take any data type
py_arr = [1,2,"Hello",3,"World"] # Valid


