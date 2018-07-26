### Fluent Python Chapter 2 Exercises

### List Comp with two for loops
colors = ['black', 'white']
sizes = ['S', 'M', 'L']
tshirts = [(color, size) for color in colors 
							for size in sizes]
print(tshirts)

### Generator expression to initialize a tuple
# Only one set of parenthesis are necessary 
symbols = '$¢£¥€¤'
ord_symbol = tuple(ord(symbol) for symbol in symbols)
print(ord_symbol)	

###generator expression to initialize an array
import array 
# The array constructor takes two arguments
# The second set of parentheses are mandatory
print_array = array.array('I', (ord(symbol) for symbol in symbols))
print(print_array)

### Generator expressions save space over list comps because they don't build the list in memory:
''' The generator expression feeds the for loop one item at a time
# This code computes the Cartesian product one item at a time
# saving the expense of building a list with n items (6 items, in this case)
# The generator expression yields items one by one; a list with all 6 t-shirt
# variations is never produced in this example.
# The colors and sizes lists are already initialized previously'''
for tshirt in ('%s %s' % (c,s) for c in colors for s in sizes):
	print(tshirt)

### Tuples as records
lax_coordinates = (33.9425, -118.408056)
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

# The % formatting operator understands tuples and treats each item as a separate
# field.
for passport in sorted(traveler_ids):
	print('%s/%s' % passport)

# prints the entire tuple record
for country in traveler_ids:
	print(country)

# prints just the country
'''The for loop knows how to retrieve the items of a tuple separately — this is
called “unpacking”. Here we are not interested in the second item, so it’s assigned
to _, a dummy variable'''
for country, _ in traveler_ids:
	print(country)
