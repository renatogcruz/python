# Implementando guloso - capítulo 8
# Código de exemplo - pág. 173 dp Bhargava

# Primeiro faça uma lista dos estados que deseja abranger:
estados_abranger = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"]) # você passa um array como entrada e ele é convertido em um conjunto
                                                                         # Set é uma collection que representa conjunto

# Você também precisa da lista de estações que podem ser escolhidas.
# Escolhi usar uma tabela hash para isso

estacoes = {}
estacoes["kum"] = set(["id", "nv", "ut"])
estacoes["kdois"] = set(["wa", "id", "mt"])
estacoes["ktres"] = set(["or", "nv", "ca"])
estacoes["kquatro"] = set(["nv", "ut"])
estacoes["kcinco"] = set(["ca", "az"])                                                                       

# Finalmente, você precisa de algo para armazenar o conjunto final de estações. Para isso você usará:
estacoes_final = set()

# Agora precisamos calcular as estacções que utilizará. Devemos escolher uma que cubra o maior número de estados
# não cobertos. 

melhor_estacao = None
estados_cobertos = set()                                #conjunto de todos os estados que essa estação abrange que ainda não foram cobertos
for estacao, estados_cobertos in estacoes.items():      #permite percorrer todas as estações para ver qual é a melhor estação
	cobertos = estados_abranger & estados_por_estacao   #isso é chamado de intersecção
	if len(cobertos) > len(estados_cobertos):
		melhor_estacao = estacao
		estados_cobertos = cobertos








