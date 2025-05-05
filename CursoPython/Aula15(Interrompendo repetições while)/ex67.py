while True:
    n = int(input('Tabuada de: '))
    print('-'*20)
    if n < 0 :
         break
    for cont in range(1,11):
     print(f'{n} x {cont} = {n*cont}')
    print('-' * 20)
print('FINALIZADO!')


