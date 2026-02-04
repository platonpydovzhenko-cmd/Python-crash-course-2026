#4.10
top = [nm ** 4 for nm in range(1, 10)]
for tt in top:
    print(tt)
print(f"These are the worst ones in the top:\n{top[:3]}")
print(f"These are the average ones in the top:\n{top[3:6]}")
print(f"These are the best ones in the top:\n{top[-3:]}")
print("----------------------------------------------------------------------------------------")
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
print("----------------------------------------------------------------------------------------")
#4.12
animes = ['Attack on Titan', 'JoJo bizzare adventure', 'Bleach', 'Naruto', 'One Piece', 'Dragon Boll']
fanime = animes[3:5]
tanime = animes[-2:]
nanime = animes[2:6]
for anime in animes:
    print(f"Anime watched:{anime}")
print("----------------")
for anim in fanime:
    print(f"First friend's favorite anime:{anim}")
print("----------------")
for ani in tanime:
    print(f"The second friend's favorite anime:{ani}")
print("----------------")
for an in nanime:
    print(f"My favorite anime:{an}")
