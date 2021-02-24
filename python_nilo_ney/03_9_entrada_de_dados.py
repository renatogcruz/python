# -*- coding: utf-8 -*-

# 3.9 leia dia, horas, minutos e segundos e retorna total em segundos

dias = int(input("Quantidade de dias: "))
horas = int(input("Quantidade de horas: "))
minutos = int(input("Quantidade de minutos: "))
segundos = int(input("Quantidade de segundos: "))

soma = dias * 86_400 +  horas * 3_600 + minutos * 60 + segundos 
     

print(f"Total em segundos é igual a {soma}") 
     
# 3.10 aumento salário
salario = float(input("Digite valor salário: "))
aumento = float(input("Digite valor aumento: "))

novo_salario = salario + (salario * aumento / 100)

print("O novo salário é de R$ ", novo_salario)

# 3.11 desconto
valor = float(input("Digite valor da mercadoria: "))
desconto = float(input("Digite valor de desconto: "))
novo_valor = valor - (valor * desconto / 100)

print("O valor do produto com desconto é de ", novo_valor)

# 3.12 tempo viagem
distancia = int(input("Qual a distância: "))
velocidade = int(input("Qual a velocidade: "))
tempo = distancia / velocidade

print(f"A viagem vai demorar {tempo} horas.")

# 3.13 converte temperatura
celsius = int(input("Entre com a temperatura em Celsus: "))
fahrenheit = (9 * celsius) / 5 + 32

print(f"A temperatura {celsius} ºC em ºF é igual a {fahrenheit}.")

# 3.14
km = int(input("Qual a quantidade de km rodados: "))
dias = int(input("Qual a quantidade de dias alugados: "))

valor = (km * 0.15) + (dias * 60)

print(f"Valor a ser pago por {km} km rodados mais {dias} dias alugado é R$ {valor}")

# 3.15
cigarros = int(input("Quantos cigarros você fuma por dia? "))
anos = int(input("Há quantos anos você fuma? "))

numero_cigarros_fumados = (anos * 365) * cigarros
tempo = numero_cigarros_fumados * 10 / 24

print(f"Você perdeu {tempo} dias da sua vida")
