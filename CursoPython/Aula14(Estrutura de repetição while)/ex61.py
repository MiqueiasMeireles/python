primeiro = int(input('1° Termo: '))
r = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(termo, end='')
    print( ' -> 'if cont <10 else '', end='')
    termo += r
    cont += 1

