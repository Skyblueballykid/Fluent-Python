# * Star operator for tuples

'''
We can prefix an argument with a star/asterisk (*) when calling a function to 
unpack a tuple
'''

# Example of tuple unpacking a function using the divmod built-in

print(divmod(20,8))

t = (20, 8)

print(divmod(*t))

quotient, remainder = divmod(*t)
print("(", quotient, ",", remainder, ")")

# Defining function parameters with *args can also be used to grab arbitrary excess arguments 

a, b, *rest = range(5)
print(a, b, rest)

a, b, *rest = range(3)
print(a, b, rest)

a, b, *rest = range(2) # rest returns an empty list
print(a, b, rest)

# The * prefix can be applied to exactly one variable, but it can appear in any position

a, *body, c, d = range(5)
print(a, body, c, d)

*head, b, c, d = range(5)
print(head, b, c, d)

