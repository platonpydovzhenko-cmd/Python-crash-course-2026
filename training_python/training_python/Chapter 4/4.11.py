#4.11
myp = ['Margherita', 'Marinara', 'Pepperoni', 'Four Cheese']
frp = myp[:]
myp.append('Hawaiian')
frp.append('Neapolitan')
for pz in myp:
    print(f"My favorite pizzas:{pz}")
print("----------------")
for pzz in frp:
    print(f"My friend's favorite pizzas:{pzz}")
