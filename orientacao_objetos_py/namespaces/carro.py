#criando classes

class Carro():
	def __init__(self, cor, portas, combustivel, potencia, qtd_combustivel, is_ligado): #método init inicializa a classe
		#definido os atributos do carro
		self.cor = cor
		self.portas = portas
		self.combustivel = combustivel
		self.potencia = potencia
		self.qtd_combustivel = qtd_combustivel
		self.is_ligado = is_ligado

	def abastecer(self):
		self.qtd_combustivel += 20

	def ligar(self):
		if self.is_ligado:
			print("O carro já está ligado.")
		else:
			self.is_ligado = True
			print("O carro foi ligado.")

	def desligar(self):
		if self.is_ligado == False:
			print("O carro já está desligado.")
		else:
			self.is_ligado = False
			print("O carro foi desligado.")




