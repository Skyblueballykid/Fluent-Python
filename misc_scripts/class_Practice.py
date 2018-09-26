# Define a class
class StreetDog:
	def __init__(self, name, age, fur):
		self.name = name
		self.age = age
		self.fur = fur

	def printme(self):
		print("Name: ", self.name, "Age: ", self.age, "Color: ", self.fur)

dog1 = StreetDog("Juno","5 months", "Brown-orange")
dog2 = StreetDog("Chiim", "6 months", "Orange-Brown")

print("Street Doges\n")
dog1.printme()
dog2.printme()
print('\n')