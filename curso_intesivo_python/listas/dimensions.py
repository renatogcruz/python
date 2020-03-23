dimensions = (200, 50) #tuplas

#print(dimensions[0])
#print(dimensions[1])

#dimensions[0] = 250 #não podemos atribuir um novo valor para um índice de tupla
print("Original dimensions:")

for dimension in dimensions:	
	print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")

for dimension in dimensions:
	print(dimension)


 