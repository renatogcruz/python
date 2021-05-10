# -*- coding: utf-8 -*-
"""
Created on Mon May 10 08:13:14 2021

@author: Renato

Exercício H - página 141

"""

# Entrada
b = int(input('Entre com valor da base: '))
e = int(input('Entre com valor do expoente: '))

# Processamnto
p = 1
cont = 1

while cont <= e:
    p = p * b
    cont = cont + 1
    
# Exibição
print(f'{b} elevado a {e} = {p}')