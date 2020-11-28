def buscaMaior(arr):
	maior = arr[0]
	maior_indice = 0
	for i in range(1, len(arr)):
		if arr[i] > maior:
			maior = arr[i]
			maior_indice = i
	return print(maior)

buscaMaior([1, 2, 3, 4, 5, 6, 8])

#com recursão

def maximo(lista):
	if len(lista) == 2:
		return lista[0] if lista [0] > lista[1] else lista[1]
	sub_max = maximo(lista[1:])
	return lista[0] if lista[0] > sub_max else sub_max

print(maximo([1, 2, 3, 4, 5, 6, 7, 8]))
