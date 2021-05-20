# -*- coding: utf-8 -*-
"""
Created on Thu May 20 08:11:44 2021

@author: Renato

# Exercício S - página 143

"""
# Entrada

dividendo = int(input("Entre com dividendo: "))
divisor = int(input("Entre com divisor: "))
cont = 1

# Processamento
while (divisor < dividendo):
    resto = dividendo - divisor
    dividendo = resto
    cont = cont + 1

# Exibição
print(f"Resultado = {cont}")
