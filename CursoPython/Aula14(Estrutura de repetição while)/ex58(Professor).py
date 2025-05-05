from random import randint
cpu = randint(0,10)
acertou = False
palpites = 0
while not acertou:
    j1 = int(input('Qual o palpite? '))
    palpites += 1
    if j1 == cpu:
        acertou = True
    else:
        if j1 < cpu:
            print('MAIS...')
        elif j1 > cpu:
            print('MENOS...')
print('Foram necessários {} palpites'.format(palpites))
