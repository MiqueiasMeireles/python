p = float(input("Peso: "))
a = float(input ('Altura: '))
imc = p/(a*a)
print('Seu IMC é {:.2f}'.format(imc))
if imc < 18.5:
  print('Abaixo do peso')
elif imc < 25:
  print('Peso ideal')
elif imc < 30:
  print('Sobrepeso')
elif imc < 40:
  print('Obeso')
else:
  print('Obesidade mórbida')
