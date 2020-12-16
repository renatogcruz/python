#implementando um grafo.
#cada vértice é conectado com um vizinho
#uma estrutura que conecta dados é uma tabela hash

grafo = {}

grafo["voce"] = ["alice", "bob", "claire"]
grafo["bob"] = ["anuj", "peguy"]
grafo["alice"] = ["peggy"]
grafo["clarice"] = ["thom", "jonny"]
grafo["anuj"] = []
grafo["thom"] = []
grafo["jonny"] = []
 
print(grafo)

