num = [[] , []]
for c in range (1,8):
    n = int(input(f'{c}° Valor: '))
    if n % 2 == 0:
        num[0].append(n)
    elif n % 2 == 1:
        num[1].append(n)
num[0].sort()
num[1].sort()
print(f'Os números pares foram {num[0]}')
print(f'Os números ímpares foram {num[1]}')
