r1 = float(input('Reta1: '))
r2 = float(input('Reta2: '))
r3 = float(input('Reta3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('{}Podem  formar um triângulo'.format('\033[32m'))
else:
    print('{}Não podem formar um triângulo{}'.format('\033[97;41m','\033[m'))