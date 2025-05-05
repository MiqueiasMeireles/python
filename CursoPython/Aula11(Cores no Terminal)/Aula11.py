print('\033[1;31;45mOlá Mundo')
print('\033[4;30;46mBom dia\033[m')
print('\033[7;97mComo vai?\033[m')
a = 3
b = 5
print('Os valores são \033[33m{}\033[m e \033[32m{}\033[m'.format(a,b))
nome = 'Miquéias'
cores = {'limpa':'\033[m',
         'azul':'\033{34m',
         'amarelo':'\033[33m',
         'preto e branco':'\033[7;97m'}
print('Seja bem-vindo {}{}{}!!!'.format('\033[4;34m',nome,'\033[m'))
print('Seja bem-vindo {}{}{}!!!'.format(cores['preto e branco'],nome,cores ['limpa']))