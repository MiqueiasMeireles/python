s = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        s = s + c
        cont = cont + 1
print('O soma dos {} valores solicidados é {}'.format(cont,s))