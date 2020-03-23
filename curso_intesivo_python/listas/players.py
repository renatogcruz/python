players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players)
print(players[0:3])
print(players[1:4])
print(players[:4]) #sem índice inical, python usa o início da lista
print(players[2:]) #sem índice final, python vai até o fim da lista
print(players[-3:]) #-n, apresenta os n últimos obejtos da lista

#percorrendo índices com um laço
print("Here are the first three players on my team:")
for player in players[:3]:
	print(player.title())





 