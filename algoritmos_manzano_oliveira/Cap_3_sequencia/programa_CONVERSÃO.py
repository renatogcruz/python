# -*- coding: utf-8 -*-
"""
Created on Wed Apr 14 08:54:12 2021

@author: Renato

Ex. 4.k - programa que apresente o valor da conversão em real de um valor 
em dólar

"""

# Entrada

d = float(input("Entre com valor em dólar: "))
c = float(input("Entre com a cotação do dólar: "))

# Processamento
r = d * c

#Exibição
print(f"O valor em real é de R$ {r:5.2f}")
