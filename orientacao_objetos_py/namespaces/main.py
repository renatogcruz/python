#herança multipla não vai ser utilizada
import carro, moto

uno_vermelho = carro.Carro('vermelho','Flex', 1.0, 4)
help(uno_vermelho.abastecer) #essa é não sabia :)
uno_vermelho.ligar()
uno_vermelho.acelerar(20)
print(uno_vermelho.velocidade)
uno_vermelho.abastecer(70)
print(f"A quantidade de combustível do carro é: {uno_vermelho.qtd_combustivel}")
del uno_vermelho

moto_vermelha = moto.Moto("vermelha", "gasolina", 1.0, 2)
moto_vermelha.ligar()
moto_vermelha.abastecer(30)
moto_vermelha.abastecer(10)
print(moto_vermelha.is_ligado)