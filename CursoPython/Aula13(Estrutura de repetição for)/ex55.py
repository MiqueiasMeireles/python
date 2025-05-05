maior = 0
menor = 0
for pessoa in range(1,4):
  peso = float(input("{}° Peso: ".format(pessoa)))
  if pessoa ==1:
    maior = peso
    menor = peso
  else:
    if peso > maior:
      maior = peso
    if peso < menor:
      menor = peso
print("\nO maior peso é {} O menor é {}".format(maior,menor))

