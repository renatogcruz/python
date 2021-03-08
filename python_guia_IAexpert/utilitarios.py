# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 08:28:19 2021

@author: Renato
"""

def soma(a, b, c):
    somatorio = a + b + c
    return somatorio

def mult(a, b, c):
    produto = a * b * c
    return produto

def divisao(a, b):
    divide = a / b
    return divide

def isPalindromo(string):
    if string == string[::-1]:
        return True
    else:
        return False
    
