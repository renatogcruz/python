a = 2
b = 2

if a > b:
	print("A é maior que B")
else:
	print("A não é maior que B")


velocidade = 85

if velocidade > 80:
	print("Você foi multado")
	print("valor da multa R$ {}" .format((velocidade - 80) * 5.00))

#imposto de renda
salario = 1200.00
base = salario
imposto = 0

if base > 3000:
	imposto = imposto + ((base - 3000) * 0.35)
	base = 3000
if base > 1000:
	imposto = imposto + ((base - 1000) * 0.20)

print(f"Salário: R${salario:6.2f} Imposto a pagar: R${imposto:6.2f}")

#caso 'else'
#minutos utilizados
minutos = 450
if minutos < 200:
	preco = 0.20
else:
	if minutos < 400:
		preco = 0.18
	else:
		preco = 0.15

print(f"Você vai pagar este mês: R${minutos * preco:6.2f}")


