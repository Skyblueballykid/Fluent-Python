import os
import sys

# some functions in the sys module
print(sys.version)
print(sys.version_info)
print(sys.platform)

# prints the current path
print(sys.argv)

for i in (sys.stdin, sys.stdout, sys.stderr):
	print(i)


# prints little or big endian byteorder 
print(sys.byteorder)

# prints the path to the python interpreter
print(sys.executable)

# A dictionary of loaded modules, can be manipulated to reload modules
print(sys.modules)

# gets the python interpreter recursion limit
print(sys.getrecursionlimit())


