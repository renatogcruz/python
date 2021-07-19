# Programa 8.3 - Cálculo do fatorial

def fatorial(n):
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat

print(fatorial(5))

# Programa 8.4 - Outra forma de calcular o fatorial

def fat(n):
    f = 1
    x = 1
    while(x <= n):
        f *= x
        x += 1
    return f

print(fat(5))

# python já têm funções para soma, máx e min
L = [5, 7, 8]
print(sum(L))
print(max(L))
print(min(L))





