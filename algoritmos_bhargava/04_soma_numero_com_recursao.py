def soma(lista):
	if lista == []:
		return 0
	else:
		return lista[0] + soma(lista[1:])


print(soma([2, 4, 6]))

lista = [2, 4, 6]

print(lista[1:])