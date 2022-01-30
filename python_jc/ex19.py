# FUNÇÕES E VARIÁVEIS - pág. 67

# # as variáveis de uma função não estão conectadas às variáveis no script.
# # veja o exercício abaixo e pense:

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket")


print("We can just give the function numbers directly")
cheese_and_crackers(20, 30)

print("OR, we can use variables from our scripts: ")
cheese_count = 10
boxes_of_crackers = 50
cheese_and_crackers(cheese_count, boxes_of_crackers)

print("We can even do math inside too: ")
cheese_and_crackers(10 + 20, 5 + 3)

print("And we can combine the two, variables and math: ")
cheese_and_crackers(cheese_count + 100, boxes_of_crackers + 1000)
