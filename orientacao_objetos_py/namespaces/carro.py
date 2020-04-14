import veiculo

class Carro(veiculo.Veiculo):
	def __init__(self, cor, tipo_combustivel, potencia, qtd_portas):
		super().__init__(cor, tipo_combustivel, potencia) #extende/subscreve métodos de uma super classe (classe pai) para a sub classe (classe filha)
		self.qtd_portas =  qtd_portas

