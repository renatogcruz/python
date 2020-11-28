def buscaMaior(arr):
	maior = arr[0]
	maior_indice = 0
	for i in range(1, len(arr)):
		if arr[i] > maior:
			maior = arr[i]
			maior_indice = i
	return print(maior)

buscaMaior([1, 2, 3, 4, 5, 6, 8])