alien_0 = {'color':'green', 'points':5} # par chave-valor {'chave':'valor'}
alien_1 = {'color':'yellow', 'points':10}
alien_2 = {'color':'blue', 'points':15}
#print(alien_0['color'])
#print(alien_0['points'])
#new_points = alien_0['points']
#print("You just earned " + str(new_points) + " pints!")

"""
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

print("The alien is " + alien_0['color'] + ".")
alien_0['color'] = 'yellow'

print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position' : 25, 'speed':'medium' }
print("Original x_position: " + str(alien_0['x_position']))
if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New x-position: " + str(alien_0['x_position']))
"""

#del alien_0['points']
#print(alien_0)

aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)