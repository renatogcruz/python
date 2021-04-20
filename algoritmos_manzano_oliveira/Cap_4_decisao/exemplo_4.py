# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 07:37:36 2021

@author: Renato

Ex. 4 - elaborar um programa que leia um valor inteiro qualquer e 
apresente esse valor soment se for dividível por 2 ou somente por 3

"""

# Entrada
n = int(input("Entre com o valor inteiro: "))

# Processamento
r2 = n % 2
r3 = n % 3


if (r2 == 0) or (r3 == 0):
   print(n)
    
