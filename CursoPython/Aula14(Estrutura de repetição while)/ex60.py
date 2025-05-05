#from math import factorial
#n =int(input('Número: '))
#f = factorial(n)
#print(f)

n = int(input('Número: '))
c = n
f = 1
while c > 0:
    print(c, end='')
    print(' x ' if c > 1 else ' = ' ,end='')
    #Traduzindo: se contador(c) for > 1 print 'x'. Se não print '='.
    f *= c
    c -= 1
print(f)