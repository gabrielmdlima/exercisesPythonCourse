from utils.utils import title, activity
title()
activity('Campeonato Brasileiro')

championship = ('Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 'Internacional', 'São Paulo',
              'Corinthians', 'Bahia', 'Cruzeiro', 'Vasco', 'Vitória', 'Atlético-MG',
              'Fluminense', 'Grêmio', 'Juventude', 'Bragantino', 'Athletico-PR',
              'Criciúma', 'Atlético-GO', 'Cuiabá')

print('-='*15)
print(f'Lista de times do Brasileirão: {championship}')
print('-='*15)
print(f'Os 5 primeiros são {championship[:5]}')
print('-='*15)
print(f'Os 4 últimos são {championship[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(championship)}')
print('-='*15)
if not 'Chapecoense' in championship:
  print('Chapecoense não está na lista de times do Brasileirão')
else:
  print(f'O Chapecoense está na {championship.index("Chapecoense")+1}ª posição')
