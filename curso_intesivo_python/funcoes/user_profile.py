def build_profile(first, last, **user_info):
	"""Constroi um dic contendo tdo que sabemos sobre um usuário"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last

	for key, value in user_info.items():
		profile[key] = value 
		return profile

user_profile = build_profile('albert', 'einstein', location='princeton', field='phisics')
print(user_profile)