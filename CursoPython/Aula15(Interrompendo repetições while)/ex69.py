e = 'S'
mais18 = H = Mmenos20 = 0
while e == 'S':
    i = int(input('Idade: '))
    g = input('Sexo [M/F]:').upper()
    e = input('Deseja continuar cadastrando? [S/N]: ').upper()
    print('-=' * 20)
    if i >= 18:
        mais18 += 1
    if g == 'M':
         H += 1
    if g == 'F' and i < 20:
        Mmenos20 += 1
print(f'{mais18} pessoas são maiores de idade.')
print(f'Foram cadastrados {H} homens.')
print(f'{Mmenos20} são mulheres com menos de 20 anos.')
