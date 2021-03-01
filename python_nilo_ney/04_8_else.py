# -*- coding: utf-8 -*-

# 4.8 - entrar com 2 valores e fazer operação escolhida

a = int(input("Entre com o primeiro valor: "))
b = int(input("Entre com o segundo valor: "))
operacao = str(input("Entre com o tipo de operação: "))

if operacao == "+":
    soma = a + b
    print(f"A soma de {a} + {b} é igual a {soma}")
elif operacao == "-":
    subtracao = a - b
    print(f"A subtração de {a} - {b} é igual a {subtracao}")
elif operacao == "*":
    multiplicacao = a * b
    print(f"A multiplicação de {a} x {b} é igual a {multiplicacao}")
elif operacao == "/":
    divisao = a / b
    print(f"A divisão de {a} / {b} é igual a {divisao}")

