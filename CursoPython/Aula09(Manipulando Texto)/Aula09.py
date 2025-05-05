frase ='Curso em Vídeo Python'
print(len(frase))
frase2 = '  Curso em Vídeo Python  '
print(len(frase2.strip())) #remove espaços inúteis
print(frase[3:13])
print(frase[:15:2])#final :2(pula de 2 em 2)
print('''Nessa aula, vamos aprender operações com String no Python. 
As principais operações que vamos aprender são o Fatiamento de''')
# aspas triplas seleciona todomum texto
print(frase.count('o'))
frase.replace('Python' ,'Android')
frase2 = (frase.replace('Python' ,'Android'))
print(frase2) #só se utilizar uma função de atribuição é possivel
# transformar uma string em mutável, se não o replace só funcionará
# uma unica vez (como fosse o inspecionar elemento do navegador)
print('Python' in frase2)