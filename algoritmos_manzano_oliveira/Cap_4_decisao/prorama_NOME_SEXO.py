# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 07:37:00 2021

@author: Renato

ex. 3.m - página 109

"""
# Entrada
nome = input("Entre com o nome: ")
sexo = input("Entre com o sexo: ")

# Processamento
if sexo == 'M' or sexo == 'F':
    if sexo == 'M':
        print(f"Ilmo. Sr. {nome}")
    else:
        print(f"Ilmo Sra. {nome}")
        