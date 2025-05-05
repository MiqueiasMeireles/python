termo = int(input('1° Termo: '))
r = int(input('Razão: '))
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += r
        cont += 1
    print('Pausa')
    mais = int(input("Quantos mostrar a mais? "))
print('Ao todo foram {} termos'.format(total))



