# -*- coding: utf-8 -*-
"""
Created on Wed May 19 08:41:59 2021

@author: Renato

Exercício Q - página 142

"""
# Entrada
continuar = "s"
total = 0

# Processamento
while (continuar == "s"):
    nome = str(input("Entre com o nome: "))
    comp = float(input("Entre com o comprimento: "))
    larg = float(input("Entre com a largura: "))
    area = comp * larg
    total = total + area
    continuar = str(input("Deseja continuar? "))
    
# Exbição
print(f"Total da área = {total} m²")


