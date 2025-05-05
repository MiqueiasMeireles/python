n = qntn = s = media = maior = menor = 0
e = 'S'
while e == 'S':
    n = int(input('Digite um número: '))
    s += n 
    qntn += 1
    if qntn == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    e = input('Quer continuar ? [S/N] ').upper()
media = s  / qntn
print('Você digitou {} números e a média foi {}'.format(qntn,media))
print(('O maior número foi {} e o menor foi {}'.format(maior,menor)))