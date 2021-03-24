# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 08:18:34 2021

@author: Renato
"""

# 5.3 interrompendo a repetição

"""
A instrução BREAK é utilizada para interromper a execução de while
"""

s = 0

while True:
    v = int(input("Digite um valor a somar ou 0 para sair: "))
    if v == 0:
        break
    s += v
print(s)

# 5.14 

contador = 0
soma = 0

while True:
    valor = int(input("Entre com valor a somar ou 0 para sair: "))
    if valor == 0:
        break
    soma += valor
    contador += 1

print(f"Números digitados: {contador}, Soma: {soma}.Média: {soma / contador}")


# 5.15 Máquina registradora

print("########################")
print("# Máquina registradora #")     
print("########################")   

total = 0

while True:
    produto = int(input("Digite código do produto ou 0 para finalizar: "))
    quantidade = int(input("Digite a quantidade de produto: "))
    if produto == 0:
        break
    elif produto == 1:
        total += 0.50 * quantidade 
    elif produto == 2:
        total += 1.00 * quantidade
    elif produto == 3:
        total += 4.00 * quantidade
    elif produto == 5:
        total += 7.00 * quantidade
    elif produto == 9:
        total += 8.00 * quantidade
    else:
        print('Valor inválido')

print(f"Valor total: R$ {total:5.2f}")



























  
