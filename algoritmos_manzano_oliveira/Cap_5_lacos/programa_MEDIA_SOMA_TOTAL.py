# -*- coding: utf-8 -*-
"""
Created on Thu May 13 08:06:52 2021

@author: Renato

Exercício N - página 142

"""

# Entrada
total = 0
soma = 0
media = 0
n = 0

# Processamento
while not n < 0:
    n = int(input("Entre com  valor: "))
    if n >= 0:
        soma = soma + n
        total = total + 1

if total > 0:
    media = soma / total
    
print(f"\nMédia = {media}. \nSoma = {soma}. \nTotal = {total}")

