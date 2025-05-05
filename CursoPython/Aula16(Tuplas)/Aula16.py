lanche = ('Hamburguer','Suco', 'Pizza', 'Pudim', 'Batata Frita')

for cont in range (0,len(lanche)):
    print(f'Vou comer um {lanche[cont]} na posição {cont}')

print('-'*25)

for posição,comida in enumerate(lanche):
    print(f'Vou comer um {comida}, na posição {posição}')
print('Agora estou satisfeito!')

print('-'*25)

print(sorted(lanche))#coloca a tupla em ordem alfabética