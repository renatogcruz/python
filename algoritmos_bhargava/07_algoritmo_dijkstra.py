#implementando o algoritmo dijkstra

grafo = {}                 # criando uma tabela hash

grafo["voce"] = ["alice", "bob", "claire"]

grafo["inicio"] = {}       # outra tabela hash para representar os pesos das arestas
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2


#print(grafo["inicio"].keys())
#print(grafo["inicio"]["a"])
#print(grafo["inicio"]["b"])

#adionando o restante dos vértices e seus vizinhos ao grafo

grafo["a"] = {}
grafo["a"]["fim"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {}        # o vértice final não tem vizinhos

# tabela hash para armazenar os custos de cada vértice

infinito = float("inf")
custos = {}
custos["a"] = 6
custos["b"] = 2
custos["fim"] = infinito

# tabela hash para os pais

pais = {}
pais["a"] = "inicio"
pais["b"] = "inicio"
pais["fim"] = None


#função para achar o custo mais barato

def ache_no_custo_mais_baixo(custos):
	custos_mais_baixo = float("inf")
	nodo_custo_mais_baixo = None
	for nodo in custos:
		custo = custos[nodo]
		if custo < custos_mais_baixo and nodo not in processados:
			custos_mais_baixo = custo
			nodo_custo_mais_baixo = nodo
	return nodo_custo_mais_baixo


#array para manter registro de todos os vértices processados

processados = []

nodo = ache_no_custo_mais_baixo(custos)      # Encontra o custo mais baixo que ainda não foi processado
while nodo is not None:                      # Caso todos os vértices tenham sido processados, esse laço será finalizado
	custo = custos[nodo]
	vizinhos = grafo[nodo]
	for n in vizinhos.keys():                # Percorre todos os vizinhos desse vértices
		novo_custo = custo + vizinhos[n]
		if custos[n] > novo_custo:            # Caso seja mais barato chegar a um vizinho a partir desse vértice ...
			custos[n] = novo_custo           # ... atualiza o custo dele
			pais[n] = nodo                   # Esse vértice se torna o novo pai para o vizinho
	processados.append(nodo)                 # Marca o vértice como processado
	nodo = ache_no_custo_mais_baixo(custos)   # Encontra o próximo vértice a ser processado e o algoritmo é repetido




