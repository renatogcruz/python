def describe_pet(animal_type, pet_name):
	"""Exibe informações sobre um animal de estimação"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry') #o argumento 'hamster' é armazenado no parâmetro pet_name
describe_pet('dog', 'wille')
describe_pet('rabbit', 'paul')
