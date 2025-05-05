n = []
while True:
    n.append(int(input('Digite um valor: ')))
    e = input('Deseja continuar? ').upper()
    if e not in 'S':
        break
print(f'Você digitou {len(n)} elementos')
n.sort(reverse=True)
print(f'Os valores em ordem decrescente são {n}')
if 5 in n:
    print('O valor 5 foi encontrado')
else:
    print('O valor 5 não foi encontrado')
