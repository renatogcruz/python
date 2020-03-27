user_0 = {'username': 'efermi', 'first': 'enrico', 'last': 'fermi'}
"""
for key, value in user_0.items(): #para escrever um laço for para um dicionário, devemos criar nomes para as duas variáveis que armazenarão a chave e o valor de cada par chave-valor
	print("\nKey: " + key)

print("Value: " + value)
"""
favorite_languages = {'jean': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}

"""
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())
	if name in friends:
		print(" hi " + name.title() + ", i see you favorite language is " + favorite_languages[name].title() + "!")
"""

"""
if 'erin' not in favorite_languages.keys():
	print("Erin, plaase take our poll!")
"""

for name in sorted(favorite_languages.keys()):
	print(name.title() + ", tank you for taking the poll.")

print("The following languages have been mentioned:")
for language in favorite_languages.values(): #sem verificar repetições
	print(language.title())
for language in set(favorite_languages.values()): #verificando repetições
	print(language.title())