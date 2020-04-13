import carro

uno_vermelho = carro.Carro('vermelho', 4, 'Flex', 1.0, 0, False, 0)
uno_vermelho.ligar()
uno_vermelho.abastecer(70)
print(f"A quantidade de combustível do carro é: {uno_vermelho.qtd_combustivel}")

uno_preto = carro.Carro('preto', 4, 'Flex', 1.4, 0, False, 0)
uno_preto.desligar()
uno_preto.acelerar(20)
uno_preto.ligar()
uno_preto.acelerar() #função com valor default
print(uno_preto.velocidade)

