# -*- coding: utf-8 -*-

# 4.1 lê dois valores e imprime qual é maior
a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
if a > b:
    print("O primeiro valor é maior")
if b > a:
    print("O segundo valor é maior")

# 4.1 se os valores forem iguais não há saída

# 4.2 carro novo ou velho, depende da idade

idade = int(input("Qual a idade do seu carro: "))

if idade <= 3:
    print("Carro novo")
if idade > 3:
    print("Carro velho")
    
# 4.2 multa excesso de velocidade

velocidade = int(input("Qual a velocidade do seu carro: "))

if velocidade > 80:
    multa = (velocidade - 80) * 5.0
    print(f"Você esta acima da velocidade. Multa de R$ {multa}")
    

