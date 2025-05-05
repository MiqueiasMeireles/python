t = int(input('Termo: '))
r = int(input('Razão: '))
décimo = t + (10-1) * r
for c in range(t, décimo + r, r):
    print('{}'.format(c), end=' -> ')
print('FIM')