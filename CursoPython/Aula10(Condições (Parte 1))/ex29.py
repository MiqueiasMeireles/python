v = float(input('Velocidade atual do carro: '))
if v <= 80:
    print('Continue com cuidado. Tenha um bom dia!')
else:
    m = 7 * (v - 80)
    (print('Velocidade excedida, voce será multado em R${:.2f}'.format(m)))
