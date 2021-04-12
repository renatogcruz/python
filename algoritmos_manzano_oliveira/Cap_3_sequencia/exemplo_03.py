# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 08:01:29 2021

@author: Renato

Ex. 3 - Desenvolver um programa que calcule o salário líquido de
um professor. Para elaborar o programa, é necessário possuir o
valor hora-aula, número de horas trabalhadas no mês e percentual
 de do INSS. Em primeiro lugar, deve-se estabelecer o seu salário
 bruto para fazer o desconto e ter o valor do líquido

"""

# programa SALRIO_PROFESSOR

# Entrada
ht = int(input("Entre com horas trabalhadas: "))
vh = float(input("Entre com valor hora aula: "))
pd = float(input("Entre com o percentual de desconto: "))

# Processamento
sb = ht * vh # salário bruto
td = (pd/100) * sb # total desconto
sl = sb - td # salário líquido

# Exibição
print(f"O salário bruto é de R$ {sb} e o liquido é de R$ {sl}")






