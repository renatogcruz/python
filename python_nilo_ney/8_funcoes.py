# criando a função
def soma(a, b):
    print(a + b)
    
# chamando função
soma(2, 9)
soma(7, 8)
soma(10, 15)

# 
def somando(a, b):
    return a + b

print(somando(2, 9))

# Função que devolve verdadeiro ou falso
def ehpar(x):
    return x % 2 == 0

print(ehpar(2))
print(ehpar(7))

# função para retornar a palavra par ou ímpar
def parouimpar(x):
    if x % 2 == 0:
        return "par"
    else:
        return "ímpar"

print(parouimpar(7))
print(parouimpar(2))

# função dentro de função
def par_impar(x):
    if ehpar(x):
        return "par"
    else:
        return "ímpar"

print(par_impar(10))
print(par_impar(5))