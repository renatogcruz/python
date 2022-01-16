from sys import argv
# execute o script passando o nome do script e o nome do filename (arquivo a ser salvo)
script, filename = argv
# prints
print(f"We're going to erase {filename}.")
print("If you don't want tha, hit CTRL - C (^C).")
print("If you do want, hit RETURN.")
# siga em frente
input("?")

print("Opening the file...")
target = open(filename, 'w')
# deleta o arquivo (se o segundo argumento for de um arquivo existente)
print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for theree lines.")
# input 3 novos valores
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")
# escreve 3 novas linhas (cada frase escrita nos inputs)
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")
# finaliza o script fechando o arquivo
print("And finally, we close it.")
target.close()
