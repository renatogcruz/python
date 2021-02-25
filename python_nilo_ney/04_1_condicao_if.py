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
    
# 4.3 cálculo do imposto de renda

salario = float(input("Digite seu salário: "))
base = salario
imposto = 0

if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000
if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)

print(f"Salário: R$ {salario:6.2f}")
print(f"Imposto a pagar: R$ {imposto:6.2f}")

# 4.3 lê 3 valores e imprimir o maior e o menor

a = int(input("Entre com primeiro valor: "))
b = int(input("Entre com segundo valor: "))
c = int(input("Entre com terceiro valor: "))

maior = a

if maior < b:
    maior = b
if maior < c:
    maior = c
print(f"O maior número é o {maior}")

menor = a 

if menor > b:
    menor = b
if menor > c:
    menor = c
print(f"O menor número é o {menor}")

# 4.4 salário aumento
salario = float(input("Entre com valor do seu salário: "))

base = 1250.00

if salario > base:
    novo_salario = salario + (salario * 10 / 100)
    print(f"Novo salário é de {novo_salario}")
if salario <= base:
    novo_salario = salario + (salario * 15 / 100)
    print(f"Novo salário é de {novo_salario}")





