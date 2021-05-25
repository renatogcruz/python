# -*- coding: utf-8 -*-
"""
Created on Sat May 22 14:30:59 2021

@author: Renato

Exemplo 1 - página 151

"""
cont = 1
lista = []

while(cont <= 10):
    valor = int(input("Entre com o valor: "))
    lista.append(valor)
    cont +=1
   

cont2 = 0
par = []
impar = []

while(cont2 < 9):
    indice = lista[cont2]
    resto = indice %2
    if resto == 0:
        multiplica = indice * 5
        par.append(multiplica)        
    else:
        soma = indice + 5
        impar.append(soma)
    cont2 += 1
        
print(par)
print(impar)

