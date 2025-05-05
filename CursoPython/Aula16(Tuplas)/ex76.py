#p == produtos e pos == posição
p = ('Farinha', 8.00 ,
     'Refri', 7.50 ,
     'Pão',  0.50 ,
     'Suco', 6.75 ,
     'Bolo', 12.00 ,
     'Rosca' , 4.50)
print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)
for pos in range(0, len(p)):
    if pos % 2 ==0:
        print(f'{p[pos]:.<30}',end='')
    else:
        print(f'R${p[pos]:>7.2f}')
print('-'*40)