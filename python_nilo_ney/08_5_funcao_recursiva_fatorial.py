# Programa 8.5 - Função recursuva do fatorial - página 167

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)
    
print(fatorial(5))
