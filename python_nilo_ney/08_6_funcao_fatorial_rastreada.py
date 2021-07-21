# Programa 8.6 - Função recursuva do fatorial rastreada - página 167

def fatorial(n):
    print(f"Calculando o fatorial de {n}")
    if n == 0 or n == 1:
        print(f"Fatorial de {n} = 1")
        return 1
    else:
        fat = n * fatorial(n - 1)
        print(f"Fatorial de {n} = {fat}")
    return fat

fatorial(4)

# A saída desse script é um bom exemplo do funcionamento de PILHA

