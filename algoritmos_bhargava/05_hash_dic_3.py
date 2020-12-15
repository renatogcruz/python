#evitando entradas duplicadas em tabelas hash

votaram = {}

valor = votaram.get("tom")   #a função get(pegar) retorna um valor se "Tom" já estiver na tabela

voted = {}

def verifica_eleitor(nome):
	if votaram.get(nome):
		print("Mande embora!")
	else:
		voted[nome] = True
		votaram[nome] = True
		print("Deixe votar!")

verifica_eleitor("tom")
verifica_eleitor("mike")
verifica_eleitor("mike")
verifica_eleitor("tom")