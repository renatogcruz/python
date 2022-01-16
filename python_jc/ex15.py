# LENDO ARQUIVOS - pá gina 51

# linhas 3 e 6 usam argv para obter um nome de arquivo - aprenderemos mais sobre o pacote sys adiante
from sys import argv

script, filename = argv

# linha 9 cria um objeto tipo 'objeto file' - pydoc open
txt = open(filename)

# a linha abaixo printa o nome do arquivo
print(f"Here's your file {filename}:")
# lê o arquivo
print(txt.read())

# abaixo, outra maneira de entrar com o nome do arquivo que desejamos ler
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

'''
lista de comandos - pág - 55
* close - fecha o arquivo
* read - lê o conteúdo do arquivo
* readline - lê apenas uma linha de um arquivo de texto
* truncate - esvazia o arquivo
* write('stuff') - escreve "stuff" no arquivo
* seek(0) - move o local de leitura/gravação para o início do arquivo
'''
