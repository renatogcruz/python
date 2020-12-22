#implementando o algoritmo grafo com a função deque

from collections import deque

def pessoa_e_vendedor(nome):
      return nome[-1] == 'm'

grafo = {}
grafo["voce"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peggy"]
grafo["alice"] = ["peggy"]
grafo["claire"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["peggy"] = []
grafo["thom"] = []
grafo["jonny"] = []

def search(nome):
    fila_de_pesquisa = deque()
    fila_de_pesquisa += grafo[nome]
    # Esse vetor é a forma pela qual você mantém o controle das pessoas que já foram verificadas.
    verificadas = []
    while fila_de_pesquisa:
        pessoa = fila_de_pesquisa.popleft()
        # Somente procure esta pessoa se você ainda não a tiver procurado.
        if pessoa not in verificadas:
            if pessoa_e_vendedor(pessoa):
                print(pessoa + " é um vendedor de manga!")
                return True
            else:
                fila_de_pesquisa += grafo[pessoa]
                # Marca esta pessoa como pesquisada
                verificadas.append(pessoa)
    return False

search("voce")




"""
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
"""