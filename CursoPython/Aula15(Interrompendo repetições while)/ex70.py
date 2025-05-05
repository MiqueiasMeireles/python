t = mais1000 = menorp = cont = 0
barato = ''
while True:
    n = input('Produto: ')
    p = float(input('Preço: R$'))
    print('=-' * 20)
    cont += 1
    t += p
    if p >= 1000:
        mais1000 += 1
    if cont == 1 or p < menorp:
        menorp = p
        barato = n
    e = ' '
    while e not in 'SN':
        e = input('\033[33mDeseja continuar? [S/N]:\033[m ').upper()
    if e in 'N':
        break

print(f'O total de gastos na compra foi R${t:.2f}')
print(f'Foram {mais1000} produtos que custam mais que R$1000.00')
print(f'O produto mais barato foi {barato} que custa R${menorp:.2f}')