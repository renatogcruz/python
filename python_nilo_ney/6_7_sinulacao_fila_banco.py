# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 08:43:18 2021

@author: Renato

Programa 6.7 simulação de uma fila de banco
página 107

"""

ultimo = 10
fila = list(range(1, ultimo + 1)) # == fila = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

while True:
    print(f"\nExistem {len(fila)} clientes na fila")
    print(f"Fila atual: {fila}")
    print("Digite F para adicionar um cliente ao fim da fila")
    print("ou A para realizar o atendimento. S para sair")
    operacao = input("Operação (F, A ou S): ")
    if operacao == "A":
        if len(fila) > 0:
            atendido = fila.pop(0) #fila atende o primeiro
            print(f"Clente {atendido} atendido")
        else:
            print("Fila vazia! Ninguém para atender")
    elif operacao == "F":
        ultimo += 1 # incrementa o ticket do novo cliente
        fila.append(ultimo)
    elif operacao == "S":
        break
    else:
        print("Operação inválida! Digite apenas F, A ou S!")
    

# exercício 6.4
# Parece continuar atendendo, mesmo sem ninguém para atender



