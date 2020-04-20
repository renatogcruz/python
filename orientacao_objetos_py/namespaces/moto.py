import veiculo

class Moto(veiculo.Veiculo):
	def __init__(self, cor, tipo_combustivel, potencia, qtd_passageiro):
		super().__init__(cor, tipo_combustivel, potencia)
		self.qtd_passageiro = qtd_passageiro
		self._libras = 30

	def abastecer(self, qtd_combustivel): #ex. de polimorfismo (subescrever)
		print("O método foi chamado a partir da classe moto (Polimorfismo)")
		if self._qtd_combustivel >= 30:
			print("A moto está com o tanque cheio")
		else:
			self._qtd_combustivel += qtd_combustivel

	def pintar(self, cor):
		if cor == 'azul':
			print("a moto não pode ser azul")
		else:
			self.cor = cor