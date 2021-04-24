# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 07:40:34 2021

@author: Renato

Ex. 3.f - página 109

"""

# Entrada
a = int(input("Entrar com valor de A: "))
b = int(input("Entrar com valor de B: "))
c = int(input("Entrar com valor de C: "))

# Processamento
if a > b:
    x = a
    a = b
    b = x
if b > c:
    x = a
    a = c
    c = x
if b > c:
    x = b
    b = c
    c = x

# Exibição
print(a, b, c)
