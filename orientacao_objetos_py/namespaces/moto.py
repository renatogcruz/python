import veiculo

class Moto(veiculo.Veiculo):
	def __init__(self, cor, tipo_combustivel, potencia, qtd_passageiro):
		super().__init__(cor, tipo_combustivel, potencia)
		self.qtd_passageiro = qtd_passageiro