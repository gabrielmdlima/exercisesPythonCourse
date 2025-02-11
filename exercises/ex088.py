from utils.utils import title, activity
title()
activity('Mega Sena')
from random import randint
from time import sleep

print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)

qtd = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=  SORTEANDO {qtd} JOGOS  -=-=-=')
jogos = list()
sorte = list()

for j in range(qtd):
  while len(sorte) < 6:
    num = randint(1,60)
    if not num in sorte:
      sorte.append(num)
  sorte.sort()
  jogos.append(sorte[:])
  sorte.clear()
  print(f'Jogo {j+1}: {jogos[j]}')
  sleep(1)
print(f'-=-=-=-=-= < BOA SORTE > -=-=-=-=-=')
