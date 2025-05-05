from random import randint
cpu = randint(1,2)
print('TENTE ACERTAR NO NÚMERO QUE ESTOU PENSANDO... [de 1 a 10]')
print('-' *57)
j = int(input('Qual o palpite?:'))
palpites = 1
while j != cpu:
   j = int(input('Errou! Tente novamente: '))
   palpites += 1
   if cpu > j:
    print('Mais... Tente Novamente')
   elif cpu < j:
    print('Menos... Tente novamente')
   else:
    print('Acertou!')
print('Foram necessários {} palpites'.format(palpites))
