from utils.utils import title, activity
title()
activity('JOGO PAR OU ÍMPAR')
from random import randint

print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')

wins = 0

while True:
  computer = randint(1, 10)
  print('=-'*15)
  player_value = int(input('Diga um valor: '))
  while True:
    player_choice = str(input('Par ou Ímpar? [P/I] ')).strip().upper()
    total = player_value + computer
    if player_choice == 'P':
      if (total) % 2 == 0:
        winner = 'player'
        category = 'DEU PAR'
      else:
        winner = 'computer'
        category = 'DEU ÍMPAR'
      break
    if player_choice == 'I':
      if not (total) % 2 == 0:
        winner = 'player'
        category = 'DEU ÍMPAR'
      else:
        winner = 'computer'
        category = 'DEU PAR'
      break

  print('-'*30)
  print(f'Você jogou {player_value} e o computador {computer}. Total de {total} {category}')
  print('-'*30)
  if winner == 'player':
    wins += 1
    print('Você VENCEU!')
    print('Vamos jogar novamente...')
  else:
    print('Você PERDEU!')
    print('=-'*15)
    print(f'GAME OVER! Você venceu {wins} vezes.')
    break
