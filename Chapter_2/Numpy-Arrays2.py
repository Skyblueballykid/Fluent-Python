import numpy as np
import sys

'''
Numpy arrays use a lot less memory than comparable lists
'''
lst = [1, 2, 3, 4, 5, 6]
numpy_array = np.array([1, 2, 3, 4, 5, 6])

sizeof_lst = sys.getsizeof(1) * len(lst) # Size = 168

sizeof_np_array = numpy_array.itemsize * numpy_array.size # Size = 48

print(sizeof_lst)

print(sizeof_np_array)