print('hello world!')
print("Yay! Printing!")

print('Hello')

# página 31
formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))

# página 33
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "\nJan\nFev\nMar\nApr\nMay\nJun\nJul"

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")

# sequências de escape
print("I am 6'2\" tall.")  # escape de aspas duplas dentro da string
print('I am 6\'2" tall.')  # escape de aspas simples dentro da string


# página 35
# \t funciona como tab
tabby_cat = "\tI'm tabbet in."
# \n pula uma linha
persian_cat = "I'm split\non a line."
# \\ separa a string com uma \. 
# Para barra comum, basta colocar apenas uma (ela não é um escape e deve funcionar apenas como caracter)
backslash_cat = "I'm \\ a \\ cat"

# \t* formata como lista
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# outros escapes ler quadro na página 36