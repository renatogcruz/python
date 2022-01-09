from sys import argv

# leia a seção 0 que vc deve ver para saber como executar isso

script, first, second, third = argv

print(f"The script is called: {script}")
print(f"Your first variable is: {first}")
print(f"Your second variable is: {second}")
print(f"Your third variable is: {third}")

print(f"\nthis is an input {input('Insert something here: ')}")

# para executar digite no ps: python ex13.py first 2nd 3rd

"""
Qual a diferença entre argv e input()?
A diferença stá relacionada a onde o usuário precisa fornecer a entrada. Se ele fornece
as entradas na linha de comando, então use argv. Se deseja que ele forneça entradas
usando o teclado enquanto o script está em execução, use input()
"""
