# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 07:28:20 2021

@author: Renato

Ex. 03 - elaborar um programa que leia 3 valores para os lados de um triângulo
e verificar se é isósceles, escaleno ou equilátero.

"""

# Entrada
a = float(input("Entre com o lado A: "))
b = float(input("Entre com o lado B: "))
c = float(input("Entre com o lado C: "))

# Processamento
if (a < b + c) and (b < a + c) and (c < a + b):
    if (a == b) and (b == c):
        print("Triângulo Equilátero")
    else:
        if (a == b) or (a == c) or (c == b):
            print("Triângulo Isósciles")
        else:
            print("Triângulo Escaleno")
else:
    print("As medidas não formam um triângulo")
    
        