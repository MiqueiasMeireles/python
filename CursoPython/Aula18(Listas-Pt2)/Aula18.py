teste = list()
teste.append('Gusta')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] ='Mari'
teste[1] = 12
galera.append(teste[:])
print(galera)