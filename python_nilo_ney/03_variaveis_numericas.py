num = 1_000_000

print(type(num))
print(1_000_000 == 1000000.00)
print(5.0 <= 5)
#print(2 ** 1_000_000)
print(3 * 0.1) # retorna 0.30000000000000004, ou seja, uma dizima periodica

print(0b10) #base 2 - binário
print(0x10) #base 16 - hexadecimal
print(0o10) #base 8 - octal

print(True or False and not True) #avalia-se 'not', 'and' e depois 'or'
print(True or False and False)    #avalia-se 'and' e depois 'or'

print(100 > 1_000 and 20 > 18)    #operadores relacionais devem ser avaliados primeiro e depois as expressões lógicas

#exercício 3.4
salario = 1_200.00
ir = 1_200.00
print(salario >= ir)

#exercício 3.6
materia1 = 4.5
materia2 = 6.0
materia3 = 7.2
media = 7.0

print(materia1 >= media and materia2 >= media and materia3 >= media)

print(len("A"))
print(len("AB"))
print(len(""))
print(len("O rato roeu a roupa"))

a = "ABCDEF"
print(a[0])
print(a[2])

#concatenação de string
print(a + "C" * 4)
#composição de string
b = 10
print("joão tem %d anos" % b)
print("%03d" % b)
print("%5f" % 5)
print("%5.2f" % 5)

nome = "joão"
idade = 22
grana = 51.34
print("%s tem %d e R$%5.2f no bolso" % (nome, idade, grana))
print("{} tem {} e R${} no bolso" .format(nome, idade, grana)) #forma mais moderna de compor strings
print(f"{nome} tem {idade} e R${grana} no bolso")              #outra maneira moderna de compor strings

