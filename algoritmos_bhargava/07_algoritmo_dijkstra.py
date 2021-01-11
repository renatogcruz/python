#implementando o algoritmo dijkstra

grafo = {}                 # criando uma tabela hash

grafo["voce"] = ["alice", "bob", "claire"]

grafo["inicio"] = {}       # outra tabela hash para representar os pesos das arestas
grafo["inicio"]["a"] = 6
grafo["inicio"]["b"] = 2


print(grafo["inicio"].keys())
print(grafo["inicio"]["a"])
print(grafo["inicio"]["b"])

#adionando o restante dos vértices e seus vizinhos ao grafo

grafo["a"] = {}
grafo["a"]["fim"] = 1

grafo["b"] = {}
grafo["b"]["a"] = 3
grafo["b"]["fim"] = 5

grafo["fim"] = {}        # o vértice final não tem vizinhos





