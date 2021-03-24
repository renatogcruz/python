# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 08:18:34 2021

@author: Renato
"""

# 5.3 interrompendo a repetição

"""
A instrução BREAK é utilizada para interromper a execução de while
"""

s = 0

while True:
    v = int(input("Digite um valor a somar ou 0 para sair: "))
    if v == 0:
        break
    s += v
print(s)

# 5.14 

contador = 0
soma = 0

while True:
    valor = int(input("Entre com valor a somar ou 0 para sair: "))
    if valor == 0:
        break
    soma += valor
    contador += 1

print(f"""Números digitados: {contador}, 
      Soma: {soma}. 
      Média: {soma / contador}""")
      
