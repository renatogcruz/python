def pesquisa_binaria(lista, item):
	baixo = 0
	alto = len(lista) -1

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

minha_lista = [1, 3, 5, 7, 9]


print(pesquisa_binaria(minha_lista, 7))


"""
caso-base = um array com apenas um elemento.
	se o item que vc procura combina com o item
	presente, vc o encontrou. Caso não, ele não está no 
	array.
caso recursivo = vc divide o array pela metade, descarta
	uma metade e faz uma pesquisa binária na outra parte
"""

def pesquisaBinaria(lista, item):
	if len(lista) == 1:
		return lista[0] if lista [0] == item else None
	# meio = corta lista no meio, descarta metade e pesquisa novamente


print(pesquisaBinaria(minha_lista, 7))