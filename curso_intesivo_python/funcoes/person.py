def build_person(fisrt_name, last_name, age=""):
	"""Devolve um dicionário com informações sobre uma pessoa"""
	person = {'first': fisrt_name, 'last': last_name}
	if age:
		person['age'] = age
	return person

musician = build_person('jimi', 'hendrix', age=27)

print(musician)

