squares = []

for value in range(1,11):
	#square = value**2
	#squares.append(square)
	squares.append(value**2) # maneira mais concisa do que a anterior, para o mesmo resultado
print("Primeira maneira: ")
print(squares)

squares_dois = [value**2 for value in range(1,11)]
print("Segunda maneira: ")
print(squares_dois)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

print(min(digits)) #valor minímo
print(max(digits)) #valor máximo
print(sum(digits)) #soma dos valores







 