# 5.2 Acumuladores

"""
A diferença entre um contador e um acumulador é que nos contadores
o valor adicionado é constante e, nos acumuladores, variável
"""

n = 1
soma = 0

while n <= 10:
    x = int(input(f"Digite o {n} número: "))
    soma = soma + x                          # é um acumulador
    n = n + 1                                # é um contador
    
print(f"Soma: {soma}")

# programa para calcular cinco variáveis

print("\nPrograma para calcular 5 variáveis")

x = 1
soma = 0

while x <= 5:
    n = int(input(f"{x} Digite o número: "))
    soma = soma + n                          #
    x = x + 1
print(f"Média: {soma / 5:5.2f}")

# Exercícios

##########################
# 5.11 programa poupança #
##########################

print("\nPrograma Poupança")

deposito = float(input("Entre com valor depositado: "))
taxa = float(input("Entre com valor da taxa de jutos: "))

print(f"Valor depositado: R$ {deposito:5.2f} e taxa de jutos {taxa} %")


ganhoTotal = deposito

cont = 1

while cont <= 24:
    ganho = deposito * taxa / 100
    ganhoTotal += ganho
    print(f"O ganho do mês {cont} foi de R$ {ganhoTotal:5.2f}")
    cont += 1

print(f"O ganho total em 24 foi de R$ {ganhoTotal:5.2f}")

#########################
# 5.12 programa poupança#
#########################


print("\n5.12 - Programa Poupança")

deposito = float(input("Faça um depósito inicial: "))
taxa = float(input("Entre com a taxa de juros: "))

saldo = deposito

cont = 1

while cont <= 24:
    # mostra saldo no mês atual
    print(f"\nSeu saldo no mês {cont} é de R$ {saldo:5.2f}")
    
    # faz deposito no mês atual
    deposito = float(input("Entre com novo depósito: "))  
    
    # Mostra valor de deposito no mês atual
    print(f"Valor depositado no mês {cont} foi de R$ {deposito:5.2f}")
    
    # calculo de taxa de juros
    rendimento = saldo * taxa / 100
    saldo += rendimento
    
    # atualiza saldo no mês atual
    saldo += deposito
    
    # contador
    cont += 1
    
############################
# 5.13 pagamento de dívida #
############################

print("############################")
print("# 5.13 pagamento de dívida #")
print("############################")

divida = float(input("Qual o valor da dívida: "))
juros = float(input("Qual a taxa de juros mensal: "))
parcela = float(input("Qual o valor da parcela: "))


dividaAtual = divida
totalPago = 0
jurosAcumulado = 0

#






