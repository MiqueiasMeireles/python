n = int(input('Número: '))
if n % 2 ==  0:
     print('Esse número é par')
else:
    print('Esse número é impar')


dv = float(input('Distância da viagem (Km)\n'))
if dv <=200:
    p = 0.50 * dv
else:
    p = 0.45 * dv
print('Uma viagem de {:.2f}Km custará R${:.2f}'.format(dv,p))

