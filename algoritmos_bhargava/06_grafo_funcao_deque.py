#implementando o algoritmo grafo com a função deque


grafo = {}

grafo["voce"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peguy"]
grafo["alice"] = ["peggy"]
grafo["clarice"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["thom"] = []
grafo["jonny"] = []
 
print(grafo)

from collections import deque
fila_de_pesquisa = deque()
fila_de_pesquisa += grafo["voce"]


def pesquisa(nome):
	fila_de_pesquisa = deque()
	fila_de_pesquisa += grafo[nome]
	verificadas = []
	while fila_de_pesquisa:
		pessoa = fila_de_pesquisa.popletft()
		if not pessoa in verificadas:
			if pessoa_e_vendedor(pessoa):
				print(pessoa + " é um vendedor de manga!")
				return True
			else:
				fila_de_pesquisa += grafo[pessoa]
		return False

pesquisa("voce")