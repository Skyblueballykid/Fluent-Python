# Tuple unpacking also allows functions to return multiple values in a way that is convenient to the caller. 

# The os.path.split() function builds a tuple (path, last_part) from a filesystem path

import os
_, filename = os.path.split('~/Users/thomaskalnik/Desktop/FluentPython-scripts/Path_split.py')

print(_)
print(filename)