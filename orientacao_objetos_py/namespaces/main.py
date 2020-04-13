import carro

uno_vermelho = carro.Carro('vermelho', 4, 'Flex', 1.0, 0, False)
uno_vermelho.ligar()
uno_vermelho.abastecer()
print(f"A quantidade de combustível do carro é: {uno_vermelho.qtd_combustivel}")

uno_preto = carro.Carro('preto', 4, 'Flex', 1.4, 0, False)
uno_preto.desligar()

