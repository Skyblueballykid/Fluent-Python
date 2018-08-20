'''
Additional helpful Numpy examples from:
 https://towardsdatascience.com/a-hitchhiker-guide-to-python-numpy-arrays-9358de570121
'''

# Numpy is useful for homogenous datasets, using multiple types won't work
numpy_arr = np.array([1,2,"Hello",3,"World"], dtype=np.int32)  # Error

# A python list can handle a variety of types 
py_arr = [1,2,"Hello",3,"World"] # Valid
