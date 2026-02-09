#5.2
p = 333
g = 'Gojo'
h = 'Hanami'
v = 467
w = 'Internet'
m = 123
nm = [p, v, m]
tt = [g, h, w]
print('------text verification------')
for tx in tt:
#1 equality
    print('--stage 1--')
    print(tx == 333)
    print(tx == 467)
    print(tx == 123)
    print(tx == 'Internet')
    print(tx == 'Gojo')
    print(tx == 'Hanami')
#1 inequality
    print(tx != 333)
    print(tx != 467)
    print(tx != 123)
    print(tx != 'Internet')
    print(tx != 'Gojo')
    print(tx != 'Hanami')
#2 lover() equality
    print('--stage 2--')
    print(tx.lover() == 333)
    print(tx.lover() == 467)
    print(tx.lover() == 123)
    print(tx.lover() == 'Internet')
    print(tx.lover() == 'Gojo')
    print(tx.lover() == 'Hanami')
#2 lover() inequality
    print(tx.lover() != 333)
    print(tx.lover() != 467)
    print(tx.lover() != 123)
    print(tx.lover() != 'Internet')
    print(tx.lover() != 'Gojo')
    print(tx.lover() != 'Hanami')
#2.1 lover() equality
    print('--stage 2.1--')
    print(tx.lover() == 333)
    print(tx.lover() == 467)
    print(tx.lover() == 123)
    print(tx.lover() == 'internet')
    print(tx.lover() == 'gojo')
    print(tx.lover() == 'hanami')
#2.1 lover() inequality
    print(tx.lover() != 333)
    print(tx.lover() != 467)
    print(tx.lover() != 123)
    print(tx.lover() != 'internet')
    print(tx.lover() != 'gojo')
    print(tx.lover() != 'hanami')
    
