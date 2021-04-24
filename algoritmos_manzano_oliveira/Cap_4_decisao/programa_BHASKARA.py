# -*- coding: utf-8 -*-
"""
Created on Sat Apr 24 07:30:28 2021

@author: Renato

Ex. 3.e - página 109

"""

# Entrada 
a = int(input("Entre com primeiro valor: "))
b = int(input("Entre com segundo valor: "))
c = int(input("Entre com terceiro valor: "))

# Processamento

if a == 0 and b == 0 and c == 0:
    print("Não há solução!")
else:
    d = b ** 2 - 4 * a * c
    if d == 0:
        x = - b / (c * a)
        print(x)
    else:
        if d > 0:
            x1 = - b / (c * a)
            x2 = + b / (c * a)
            print(f"x1 = {x1}")
            print(f"x2 = {x2}")
        else:
            print("Não existe raizes reais!")
