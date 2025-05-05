n =[]
for num in(range(0,5)):
    n.append(int(input(f'Digite um número na posição {num}: ')))
    maior = max(n)
    menor = min(n)
print(f'O maior número é {maior} na posição',end=' ')
for pos, num in enumerate(n):
    if num == maior:
        print(f'{pos}...',end=' ')
print(f'\nO menor número é {menor} na posição',end=' ')
for pos, num in enumerate(n):
    if num == menor:
        print(f'{pos}...',end=' ')



