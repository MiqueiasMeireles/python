from operator import index
from os.path import split

tabela = ('Palmeiras', 'Corinthians', 'Atlético-MG', 'Fluminense', 'Athletico-PR', 'Flamengo',
          'internacional', 'Bragantino', 'São Paulo', 'Santo', 'Botafogo', 'Ceará SC', 'Goiáis', 'Avaí', 'Cuibá',
          'Coritiba', 'Améria-MG', 'Atlético-GO', 'Fortaleza', 'Juventude')
print('-='*50)
print(f'Lista de times do Brasileirão: {tabela}')
print('-='*50)
print(f'Os 5 primeiros são: {tabela[:5]}')
print('-='*50)
print(f'Os 4 últimos são: {tabela[-4:]}')
print('-='*50)
print(f'Em ordem alfabética: {sorted(tabela)}')
print('-='*50)
print(f'O Fluminense esta na {tabela.index("Fluminense")+1}° posição')
print('-='*50)