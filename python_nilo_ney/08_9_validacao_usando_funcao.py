# Programa 8.9 - Exemplo de validação com uma função


def faixa_int(pergunta, minimo, maximo):
    while True:
        v = int(input(pergunta))
        if v < minimo or v > maximo:
            print("Valor inválido")
        else:
            return v

faixa_int(10, 0, 5)