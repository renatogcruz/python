#programa de uma fila de banco

ultimo = 10
fila = list(range(1, ultimo + 1))


while True:
	print(f"\nExistem {len(fila)} clientes na fila")
	print(f"Fila atual: {fila}")
	print("Digite 1 para adicionar um cliente ao fim da fila,")
	print("ou 2 para realizar o atendimento. 3 para sair")
	operacao = input("Operação (1, 2 ou 3):")
	if operacao == 1:
		if len(fila) > 0:
			atendimento = fila.pop(0)
			print(f"Cliente {atendimento} atendido")
		else:
			print("Fila vazia! Ningém para atender")
	elif operacao == 2:
		ultimo += 1 #incrementa o ticket do novo cliente
		fila.append(ultimo)
	elif operacao == 3:
		break
	else:
		print("Operação inválida! Digite apenas 1, 2 ou 3")

