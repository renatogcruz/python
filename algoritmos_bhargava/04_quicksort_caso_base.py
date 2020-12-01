#arrays vazios ou com 1 elementos serão o caso-base

def quicksort(array):
	if len(array) < 2:
		return array


print(quicksort([]))
print(quicksort([20]))