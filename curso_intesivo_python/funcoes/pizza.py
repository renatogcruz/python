def make_pizza(*toppings): #o asterisco no nome diz a python para criar uma tupla vazia chamada toppings e reunir os valores recebidos nessa tupla
	"""Exibe a lista de ingredientes pedidos"""
	#print(toppings)

#make_pizza('pepperoni')
#make_pizza('mushrooms', 'green peppers', 'extra cheese')
	"""Apresentar a pizza que estamos prestes a preparar"""
	print("\nMaking a pizza with the following toppings:")

#for toppings in toppings:
	print("- " + toppings)

	make_pizza('pepperoni')
	make_pizza('mushrooms', 'green peppers', 'extra cheese')


