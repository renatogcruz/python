# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 07:11:15 2021

@author: Renato

3.c - calcular média de 4 notas e exibir se aprovado ou não

"""

# Entrada
a = float(input("Entre com a primeira nota: "))
b = float(input("Entre com a segunda nota: "))
c = float(input("Entre com a terceira nota: "))
d = float(input("Entre com a quarta nota: "))

# Processamento
media = (a + b + c + d) / 4

if media >= 5.00:
    print("Aprovado")
else:
    print("Reprovado")
