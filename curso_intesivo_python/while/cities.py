prompt = "\nPlease enter the name of a city you have visited"

prompt += "\nEnter 'wuit' to end the program"


while True:
	city = input(prompt)
	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!")
	

