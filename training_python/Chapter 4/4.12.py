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
