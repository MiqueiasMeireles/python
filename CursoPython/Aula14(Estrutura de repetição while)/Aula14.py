e = 'S'
n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
    if e == 'S':
            print('Parar?')
            e = input().upper()
print(par, impar)
print('Fim')