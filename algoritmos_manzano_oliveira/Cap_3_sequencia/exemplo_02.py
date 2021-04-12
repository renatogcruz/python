# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 07:52:49 2021

@author: Renato

Ex. 2 - Elaborar um programa de computador que calcule a área de uma 
circunferência eapresentar a medida da área calculada.


"""

# programa AREA_CIRCULO

# Constante
pi = 3.14159265

# Entrada
r = float(input('Entre com o raio: '))

# Processamento
a = pi * r ** 2

# Exibição
print(f"A área da circulo é igual a {a}")