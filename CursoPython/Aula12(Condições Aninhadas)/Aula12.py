n = str(input('Digite se Nome: '))
if n == 'Miquéias':
    print('Que belo nome!')
elif n == 'Gaga' or 'Gogo' or 'Gigi':
    print('Que nome estranho!')
elif n in 'Malu' 'Lala' 'Lulu':
    print('Vejo que isso é um apelido. Certo?')
else:
    print('Que nome normal...')
print('Seja Bem-Vindo,\033[;33m{}'.format(n))