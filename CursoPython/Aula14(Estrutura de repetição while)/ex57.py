str(input('Sexo [M/F]:')).strip().upper()
s = ['M','F']
while s not in ['M','F']:
    s = input('Inválido, digite novamente: ').upper()
print('Sexo [{}] registrado!'.format(s))