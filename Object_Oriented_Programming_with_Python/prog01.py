class Class01:

	def __init__(self):
		print("Just created an objetc for Class01...")

class Class02:

	def __init__(self):
		print("Just created an object for Class02...")

def main():
	o1 = Class01()
	o2 = Class02()

if __name__ == "__main__":
	print("Module prog01 is being run directly...")
	main()
else:
	print("Module prog01 has been imported in the current module...")