# -*- coding: utf-8 -*-
"""
Created on Mon Apr 26 07:19:50 2021

@author: Renato

Ex. 3.i - página 109

"""

# Entrada
a = int(input("Entre com valor de A: "))
b = int(input("Entre com valor de B: "))
c = int(input("Entre com valor de C: "))
d = int(input("Entre com valor de D: "))
e = int(input("Entre com valor de E: "))

# Processamento
maior = a

if maior < b:
    maior = b   
if maior < c:
    maior = c
if maior < d:
    maior = d
if maior < e:
    maior = e
menor = a
if menor > b:
    menor = b
if menor > c:
    menor = c
if menor > d:
    menor = d
if menor > e:
    menor = e

# Exibição
print(f"Maior: {maior}. Menor: {menor}")













