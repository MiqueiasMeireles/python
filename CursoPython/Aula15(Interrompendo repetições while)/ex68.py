from random import randint
v = 0
while True:
    cpu = randint(0,10)
    n = int(input('Escolha um número: '))
    t = n + cpu
    ip = ' '
    while ip not in 'PI':
        ip = input('Ímpar ou Par? [I/P]: ').upper()
    print(f'Você escolheu {n} e o computador escolheu {cpu}. Total {t}', end='')
    print(' [PAR]' if t % 2 == 0 else ' [ÍMPAR]')
    if ip == 'P':
        if t % 2 == 0:
            print('\033[33mVenceu\033[m')
            v += 1
        else:
            print('\033[32mPerdeu\033[m')
            break
    elif ip == 'I':
        if t % 2 == 1:
            v += 1
            print('\033[33mVenceu\033[m')
        else:
            print('\033[31mPerdeu\033[m')
            break
    print('Vamos Novamente...')
print(f'GAME OVER! Você venceu {v} vezes')


