n1 = int(input('1° Número: '))
n2 = int(input('2° Número: '))
e = 0
while e != 5:
    print('''  [1] SOMA 
  [2] MULTIPLICAÇÃO 
  [3] MAIOR 
  [4] NOVOS NÚMEROS
  [5] SAÍDO''')
    e = int(input("Escolha: "))
    if e == 1:
        s = n1 + n2
        print('Entre {} e {} o resultado é {}'.format(n1, n2, s) )
    elif e == 2:
        m = n1 * n2
        print('Entre {} e {} o resultado é {}'.format(n1, n2,m))
    elif e == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2,maior))
    elif e == 4:
        print('Informe os números novamente!')
        n1 = int(input('1° Número: '))
        n2 = int(input('2° Número: '))
    elif e ==5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    print('Programa finalizado')

