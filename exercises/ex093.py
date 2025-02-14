from utils.utils import title, activity
title()
activity('Aproveitamento do jogador')

ficha = dict()
ficha['nome'] = str(input('Nome do Jogador: ')).strip()
gols = list()
total = 0
partidas = int(input(f'Quantas partidas {ficha["nome"]} jogou? '))
for i in range(partidas):
  gols.append(int(input(f'Quantos gols na partida {i}? ')))
  total += gols[i]
ficha['gols'] = gols
ficha['total'] = total
print('-='*30)
print(ficha)
print('-='*30)
for k, v in ficha.items():
  print(f'O campo {k} tem o valor {v}.')
print('-='*30)
print(f'O jogador {ficha["nome"]} jogou {partidas} partidas.')
for i, g in enumerate(ficha['gols']):
  print(f'    => Na partida {i}, fez {g} gols.')
print(f'Foi um tolal de {total} gols.')
