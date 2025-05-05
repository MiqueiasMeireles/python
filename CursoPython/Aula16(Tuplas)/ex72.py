ne = ('zero', 'um', 'dois', 'três', 'quatro',
      'cinco', 'seis', 'sete', 'oit', 'nove','dez')
while True:
    n = int(input('Digite um número de 0 a 10: '))
    if 0 <= n <=10:
        print(f'Você digitou o número {ne[n]}')
    else:
        print('\033[33mInválido. Por favor digite números entre 0 e 10 \033[m')
    e = ' '
    while e not in 'SN':
        e = input('Deseja continuar? [S/N]: ').upper()
    if e in 'N':
        break
print('Finalizado!')