#código para o quicksort

def quicksort(array):
	if len(array) < 2:
		return array                                            #caso-base -> arrays com 0 ou 1 elemento

	else:
		pivo = array[0]                                         #caso recursivo (ps. escolher o primeiro array não é uma boa ideia)
		menores = [i for i in array[1:] if i <= pivo]           #subarray de todos os elementos menores do que o pivô
		maiores = [i for i in array[1:] if i > pivo]            #subarray de todos os elementos maiores do que o pivô
		return quicksort(menores) + [pivo] + quicksort(maiores) #ordenamento 

print(quicksort([10, 5, 2, 3, 7, 1, 33]))
	