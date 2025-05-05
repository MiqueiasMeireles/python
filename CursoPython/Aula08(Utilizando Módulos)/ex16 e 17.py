from math import trunc, sqrt, hypot
n = float(input('Digite um número: '))
parti = n
print('O número {} tem a parte inteira {}'.format(n, trunc(parti)))

y = float(input('Cateto Oposto: '))
x = float(input('Cateto Adjacente: '))
r = hypot(sqrt(x*x + y*y))
print('{:.3f}'.format(r))
