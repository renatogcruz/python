motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#motorcycles[0] = 'ducati' #altera o valor do primeiro item para 'ducati'

#motorcycles.append('ducati') #inseri o valor 'ducati' no final da lista

#motorcycles.insert(0, 'ducati') #inseri o valor 'ducati' no ínicio da lista

#del motorcycles[0] # o primeiro valor é  apagado da lista

#popped_motorcycle = motorcycles.pop() #fazemos pop (remove o último item de uma lista) de um valor da lista e o armazenamos na variável popped_motorcycle
#print(motorcycles)

#last_owned = motorcycles.pop(0) #podemos acrescentar ou não valores ao pop, se não acrescer escolhe o último valor
#print("The last motorcycles I owned was a " + last_owned.title() + ".")

#motorcycles.remove('suzuki') #python descobre em que lugar 'suzuki' aparece na lista e remove esse elemento
#print(motorcycles)

too_expensive = 'suzuki'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + " is too expensive for me")




 