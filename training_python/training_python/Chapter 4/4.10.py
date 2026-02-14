#4.10
top = [nm ** 4 for nm in range(1, 10)]
for tt in top:
    print(tt)
print(f"These are the worst ones in the top:\n{top[:3]}")
print(f"These are the average ones in the top:\n{top[3:6]}")
print(f"These are the best ones in the top:\n{top[-3:]}")
