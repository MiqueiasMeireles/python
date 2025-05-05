num = []
while True:
    n = int(input('Número: '))
    if n not in num:
        num.append(n)
    e = input('Continuar? ').upper()
    if e not in 'S':
        break
num.sort()
print(num)