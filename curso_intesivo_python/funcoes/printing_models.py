unprinted_designs = ['iphone case', 'robot pendat', 'dodecahedron']

completed_models = []

while unprinted_designs:
	current_design = unprinted_designs.pop()
	print("Printing model: " + current_design)

print("\nThe following models have been printed:")
for completed_models in completed_models:
	print(completed_models)



