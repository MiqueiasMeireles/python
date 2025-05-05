from random import randint
lista = []
jogos = []
cont = 0
e = int(input('Quantos jogos quer sortear? '))
print('='*31)
tot = 1
while tot <= e:
    cont = 0
    while True:
        n = randint(1,60)
        if n not in lista:
            lista.append(n)
            cont +=1
        if cont >=6 :
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
for i, l in enumerate(jogos): # i(índice) , l(lista)
    print(f'Jogo {i+1}: {l}')