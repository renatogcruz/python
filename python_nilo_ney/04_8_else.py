# -*- coding: utf-8 -*-

# 4.8 - entrar com 2 valores e fazer operação escolhida

a = int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o segundo valor: "))
operacao = str(input("Entre com o tipo de operação: "))

if operacao == "+":
    soma = a + b
    print(f"A soma de {a} + {b} é igual a {soma}")
elif operacao == "-":
    subtracao = a - b
    print(f"A subtração de {a} - {b} é igual a {subtracao}")
elif operacao == "*":
    multiplicacao = a * b
    print(f"A multiplicação de {a} x {b} é igual a {multiplicacao}")
elif operacao == "/":
    divisao = a / b
    print(f"A divisão de {a} / {b} é igual a {divisao}")

# 4.9 - Aprovar empréstimo bancário

valor_casa = float(input("Entre com valor da casa: "))
salario = float(input("Entre com valor do salário: "))
anos = int(input("Entre com o tempo para pagar (em anos): "))

salario_trinta = salario * 0.30
valor_anos = valor_casa / (anos * 12)

if salario_trinta >= valor_anos:
    print(f"As prestações serão de R$ {valor_anos:6.2f}")
    print(f"30% do seu salário é igual a R$ {salario_trinta:6.2f}")
    print("Financiamento aprovado!")
else:
    print(f"As prestações serão de R$ {valor_anos:6.2f}")
    print(f"30% do seu salário é igual a R$ {salario_trinta:6.2f}")
    print("Financiamento reprovado!")
    
# 4.10 energia elétrica

quantidade = int(input("Entre com a quantidade de kWh: "))
tipo = str(input("Entre com o tipo de instalação: "))

if tipo == "R":
    if quantidade <= 500:
        print("Preço a pagar é de R$ ", quantidade * 0.40)
    else:
        print("Preço a pagar é de R$ ", quantidade * 0.65)
elif tipo == "C" :
    if quantidade <= 1000:
        print("Preço a pagar é de R$ ", quantidade * 0.55)
    else:
        print("Preço a pagar é de R$ ", quantidade * 0.60)
else:
    if quantidade >= 5000:
        print("Preço a pagar é de R$ ", quantidade * 0.55)
    else:
        print("Preço a pagar é de R$ ", quantidade * 0.60)
    
    
    
    
    