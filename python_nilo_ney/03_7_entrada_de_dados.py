# -*- coding: utf-8 -*-

# 3.7 entrada de dados
x = input("Digite seu nome: ")
print(x)

print(f"Você digitou {x}")
print(f"Olá, {x}")

# 3.7.1 conversão da entrada de dados
anos = int(input("Anos de serviço: "))
valor_por_ano = float(input("Valor por ano: "))
bonus = anos * valor_por_ano
print(f"Bônus de R$ {bonus:5.2f}")

# 3.7 faça um programa que peça 2 numeros inteiros. Imprima a soma
number1 = int(input("Entre com o primeiro número: "))
number2 = int(input("Entre com o segundo número: "))
soma = number1 + number2
print(f"A soma de {number1} + {number2} é igual a {soma}")

# 3.8 lê em metros e exibe em milímetros
valor = int(input("Entre com valor em metros: "))
converte = valor * 1000
print(f"O valor {valor} m em mílimetro é igual a {converte}.")

