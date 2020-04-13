#criando classes

class Carro():
	def __init__(self, cor, portas, combustivel, potencia, qtd_combustivel, is_ligado, velocidade): #método init inicializa a classe
		#definido os atributos do carro
		self.cor = cor
		self.portas = portas
		self.combustivel = combustivel
		self.potencia = potencia
		self.qtd_combustivel = qtd_combustivel
		self.is_ligado = is_ligado
		self.velocidade = velocidade

	def abastecer(self, qtd_combustivel):
		print(f"O carro possui {self.qtd_combustivel} litros de combustível")
		self.qtd_combustivel += qtd_combustivel

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

	def acelerar(self, velocidade=10):
		if self.is_ligado:
			self.velocidade += velocidade
		else:
			print("O carro precisa ser ligado para acelerar.")



