#3.10
j_f = ['Dango', 'Sushi', 'Ramen', 'Daifuku', 'Mochi']
print(f"Our menu includes:{j_f}")
print(f"Our menu includes:{sorted(j_f)}")
print(f"Our menu includes:{sorted(j_f, reverse=True)}")
j_f.reverse()
print(f"Our menu includes:{j_f}")
j_f.reverse()
print(f"Our menu includes:{j_f}")
j_f.sort()
print(f"Our menu includes:{j_f}")
j_f.sort(reverse=True)
print(f"Our menu includes:{j_f}")
print(len(j_f))
