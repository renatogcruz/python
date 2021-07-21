# Programa 8.8 - Exemplo de validação sem usar uma função

while True:
    v = int(input("Digite um valor entre 0 e 5: "))
    if v < 0 or v > 5:
        print("Valor inválido")
    else:
        break