name = "ada lovelace"
nome = "RENATO CRUZ"

print(name.title()) #title() exibe cada palavra com uma letra maiúscula no início
print(nome.title())

print(name.upper()) #upper() exibe cada palavra com letras maiúscula
print(name.lower()) #lower() exibe cada palavra com letras minúscula

first_name = "ada"
last_name = "lovelace"

full_name = first_name + " " + last_name # usamos o + para Combinando ou concatenando strings
print(full_name)

print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

#Acrescentando espaços em branco em strings com tabulações ou quebras de linha
print("Python")
print("\nPython")
print("\n")
print("Languages:\n\tPython\n\tC\n\tJavaScript") #"\n\t" diz a Python para passar para uma nova
#linha e iniciar a próxima com uma tabulação

#Removendo espaços em branco
favorite_language = ' python '
print(len(favorite_language))
print(len(favorite_language.rstrip())) #removemos os espaços extras do lado direito
print(len(favorite_language.lstrip())) #removemos os espaços extras do lado esquerdo
print(len(favorite_language.strip()))  #removemos os espaços extras dos dois lados






 