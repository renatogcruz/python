ten_things = 'Apples Oranges Crows Telephone Light Sugar'

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song",
              "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])

# pop () é usado para remover um elemento na lista (por padrão, o último elemento)
print(stuff.pop())

# join() é um método de string e retorna uma string na qual os elementos da sequência
# foram unidos por um separador str
print(' '.join(stuff))
print('#'.join(stuff[3:5]))
