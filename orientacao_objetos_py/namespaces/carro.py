import veiculo

class Carro(veiculo.Veiculo):
	def __init__(self, cor, tipo_combustivel, potencia, qtd_portas):
		super().__init__(cor, tipo_combustivel, potencia) #extende/subscreve métodos de uma super classe (classe pai) para a sub classe (classe filha)
		self.qtd_portas =  qtd_portas
		
	def abastecer(self, qtd_combustivel):
		print("O método foi chamado a partir da classe carro (Polimorfismo)")
		self._qtd_combustivel += qtd_combustivel

	def pintar(self, cor):
		if cor == "preto":
			print("O carro não pode ser preto")
		else:
			self._cor = cor

#sobrescrita de métodos abstratos em classes-filha (o método abstrato sobrescrito se sobre sai ao métod da classe-pai)