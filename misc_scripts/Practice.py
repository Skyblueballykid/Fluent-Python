x = 2

# Define a function
def squared_x(x):
	y = x ** 2
	print(y)

squared_x(x)


# Define a list
a1 = []
a2 = list()

# Define a Dict
b1 = {}
b2 = dict()

# List Comp
a3 = [x for x in range(10)]
print(a3)

# Dict comp
b3 = {str(x):x for x in a3}
print(b3)