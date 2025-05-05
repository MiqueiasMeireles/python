n = str(input('Nome completo: ')).strip()
print('Analisando...')
print('Seu nome em maiúsculas é ',n.upper())
print('Seu nome em minúsculasé ',n.lower())
print('Seu nome tem ao todo ',len(n)-n.count(' '),'letras')
dividido = n.split()
print('Seu primeiro nome é ',dividido[0],'e tem', len(dividido[0]),'letras')
print('Seu primeiro nome é {} e tem {} letras'.format(dividido[0]), len(dividido[0]))

