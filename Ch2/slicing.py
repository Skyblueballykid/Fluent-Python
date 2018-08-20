# advanced slicing

# slicing of both lists and ranges

# splitting a list

l = [20, 30, 40, 50, 60]
print(l[:2]) # split at 2

print(l[:3]) # split at 3

print(l[3:]) # print all items from position 3 on

# Slice objects
s = 'bicycle'
print(s[::3]) # prints 'bye'

print(s[::-1]) # prints 'elcycib'

print(s[::-2]) # prints 'eccb'

# the [] operator can take multiple indexes or slices separated by commas
# in numpy arrays, items can be fetched like:
# a[i, j]
# a two dimensional slice:
# a[m:n, k:l]

# if x is a 4 dimensional array:
# x[i, ...] is a shortcut for x[i, :, :, :,]

l = list(range(10))
print(l)

del l[5:7]

l[3:2] = [11, 22]
print(l)

l[2:5] = [100]
print(l)

# when the target of the assignment is a slice, the right-hand side must be an # iterable object, even if it has just one item. 
