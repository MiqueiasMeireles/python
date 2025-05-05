n = []
par = []
impar = []
while True:
    n.append(int(input('Digite um número: ')))
    e = input('Quer continuar? ').upper()
    if e in 'N':
        break
for i,v in enumerate(n): # i: índice(são os números que indicam a posição do item na lista, começando do 0 ao... , v: valor
    if v % 2 == 0:
        par.append(v)
    elif v % 2 == 1:
        impar.append(v)
print(f'A lista completa é {n}')
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
