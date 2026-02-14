#5.2
p = 333
g = 'Gojo'
h = 'Hanami'
v = 467
w = 'Internet'
m = 123
n = 111117
l = 'Levi'
nm = [p, v, m]
tt = [g, h, w]
print("----==----")
print(g == p)#f
print(v == p)#f
print(p == p)#t
print("----!=----")
print(g != p)#t
print(v != p)#t
print(p != p)#f
print("----lower. != ==----")
print(g.lower() == 'Gojo')#f
print(w.lower() == 'internet')#t
print(h.lower() == 'Hanami')#f
print(g.lower() != 'Gojo')#t
print(w.lower() != 'internet')#f
print(h.lower() != 'Hanami')#t
print("----1 == 1----")
print(v == p)#f
print(p == m)#f
print(p == 333)#t
print("----1 != 1----")
print(v != 466)#t
print(m != m)#f
print(p != 333)#f
print("----1 <= 1----")
print(v <= 466)#f
print(p <= 334)#t
print(v <= 333)#f
print("----1 >= 1----")
print(m >= 466)#f
print(m >= m)#t
print(p >= 1000)#f
print("----1 > 1----")
print(v > 466)#t
print(p > m)#t
print(v > 1233)#f
print("----1 < 1----")
print(p < 400)#t
print(v < m)#f
print(v < 56777)#t
print("----or and----")
print(w == 'Internet' or w == 'Gojo')#t
print(m == 124 and m >= 10)#f
print(m != h or m == h)#t
print(g == 'Gojo' and g != m)#t
print("----if----")
if m not in nm:
    print('false')
if g in tt:
    print('true')
if l in nm:
    print('false')
if n in tt:
    print('false')
