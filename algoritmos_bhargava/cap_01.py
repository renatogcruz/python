def pesquisa_binaria(lista, item):
	baixo = 0
	alto = len(lista) - 1

	while baixo <= alto:
		meio = (baixo + alto) // 2
		chute = lista[meio]
		if chute == item:
			return meio
		if chute > item:
			alto = meio - 1
		else:
			baixo = meio + 1
	return None

minha_lista = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]

print(pesquisa_binaria(minha_lista, 21))

print(15/2)
print(15//2)
