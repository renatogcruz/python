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
