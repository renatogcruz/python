import heapq

class FilaDePrioridade:

	def __init__(self):
		self.fila = []
		self.indice = 0

	def inserir(self, item, prioridade):
		heapq.heappush(self.fila,(-prioridade, self.indice, item))

	def remover(self):
		return heapq.heappop(self.fila)[-1]

class Item:

	def __init__(self, nome):
		self.nome = nome

	def __repr__(self):
		return self.nome

fila = FilaDePrioridade()
fila.inserir(Item('marcos'), 28)
fila.inserir(Item('joao'), 30)
fila.inserir(Item('maria'), 18)

print(fila.remover())

