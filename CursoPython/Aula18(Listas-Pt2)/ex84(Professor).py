pessoas = []
dados = []
maior = menor = 0
while True:
    dados.append(input('Nome: ').capitalize())
    dados.append(int(input('Peso: ')))
    e = input('Continuar? ')
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    if e in 'Nn':
        break
print('¨'*20)
print(f'O total de pessoas cadastradas foram {len(pessoas)}')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]',end=' ')
print(f'tem o maior peso com {maior}Kg')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]', end=' ')
print(f'tem menor peso com {menor}Kg')
