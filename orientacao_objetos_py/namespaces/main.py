#herança multipla não vai ser utilizada
import carro, moto

uno_vermelho = carro.Carro('vermelho','Flex', 1.0, 4)
help(uno_vermelho.abastecer) #essa é não sabia :)
uno_vermelho.ligar()
uno_vermelho.acelerar(20)
uno_vermelho._libras
#uno_vermelho.qtd_combustivel(200) # o atributo privado serve para impedir esse tipo de comando (só se enche o tanque abastecendo)

del uno_vermelho

moto_vermelha = moto.Moto("vermelha", "gasolina", 1.0, 2)
moto_vermelha.ligar()
