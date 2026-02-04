#4.13
buffet = ('trout', 'wine', 'fried eggs', 'tea', 'Coca-Cola')
for food in buffet:
    print("This is the old menu:")
    print(food)
print("-----------")
buffet = ('trout', 'wine', 'fried eggs', 'coffe', 'pepsi')
for food in buffet:
    print("this is the new menu:")
    print(food)
#кортеж не изменяемый а заменяемый
print("-----------")
buffet[0] = 'apple'

