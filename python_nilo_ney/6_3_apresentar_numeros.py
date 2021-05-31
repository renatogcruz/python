# -*- coding: utf-8 -*-
"""
Created on Mon May 31 08:09:52 2021

@author: Renato

programa 6.3 - apresentação de números - página 99

"""
numeros = [0, 0, 0, 0, 0]
cont = 0

while cont < 5:
    numeros[cont] = int(input(f"Número {cont + 1}: "))
    cont += 1
    
while True:
    escolhido = int(input("Que posição você quer imprimir (0 para sair): "))
    if escolhido == 0:
        break
    print(f"Você escolheu o número: {numeros[escolhido - 1]}")



