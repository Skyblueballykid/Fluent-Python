import math
import numpy as np
import pandas

'''
A script to brute-force passwords
'''

# Password. Could also take raw input or use selenium to input into a web page
pw = ["A", "X", "E", "I", "O", "1", "2", "3"]

low_letter_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", \
		 		   "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

upper_letter_list = [x.capitalize() for x in low_letter_list]

num_list = [str(x) for x in range(10)]

combined_list = list()

combined_list.extend(low_letter_list)
combined_list.extend(upper_letter_list)
combined_list.extend(num_list)

# print(combined_list)

length = len(combined_list)

# Iterate over the list and compare each character to the password characters
for x in combined_list:
	for y in pw:
		if x == y:
			print(x, "yes")
		else:
			pass



	