def get_formatted_name(first_name, middle_name, last_name):
	"""Devolve um nome completo formado de modo elegante"""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name =	first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('john', 'lee')
print(musician)

musician = get_formatted_name('john', 'lee', 'hooker')
print(musican)
