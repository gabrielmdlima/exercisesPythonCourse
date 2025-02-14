from utils.utils import title, activity
title()
activity('Aproveitamento do jogador v2')

jogadores = list()
jogador = dict()

while True:
  print('-'*30)
  gols = list()
  total = 0
  jogador['nome'] = str(input('Nome: ')).strip().capitalize()
  
  partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
  for i in range(partidas):
    gols.append(int(input(f'Quantos gols na partida {i}? ')))
    total += gols[i]
  jogador['gols'] = gols[:]
  jogador['total'] = total

  jogadores.append(jogador.copy())

  while True:
    stay = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if stay in 'SN':
      break
  if stay == 'N':
    break
print('-='*30)
print(f'cod {"nome":<15}{"gols":<15}{"total":<6}')
print('-'*40)
for i, j in enumerate(jogadores):
  print(f'{i:>3} {j["nome"]:15}{str(j["gols"]):15}{j["total"]}')

while True:
  print('-'*40)
  select = int(input('Mostrar dados de qual jogador? '))
  if select == 999:
    break
  elif select < 0 or select >= len(jogadores):
    print(f'ERRO! Não existe jogador com código {select}! Tente novamente')
  else:
    print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[select]["nome"]}:')
    for j, g in enumerate(jogadores[select]['gols']):
      print(f'   No jogo {j} fez {g} gols.')
print('<< VOLTE SEMPRE >>')
