soma = 0
cont = 0
for c in range(1, 4):
    n = int(input('{}° Número: '.format(c)))
    if n % 2 ==0:
        soma = soma + n
        cont = cont + 1
print('Foram {} PARES somando {} '.format(cont,soma))
