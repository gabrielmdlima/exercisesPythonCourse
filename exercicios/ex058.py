from utils.utils import title, activity
title()
activity('Jogo de advinhação')
from random import randint

computer = randint(0, 10)
player = 11
count = 0

while player != computer:
  player = int(input('Qual o seu palpite? '))
  count += 1

print(f'PARABÉNS! O número era {computer} e você acertou em {count} tentativas!')
input('\nPressione enter para ir para a correção.')

#  Correção do exercício
title()
activity('Correção do exercício')

#  from random import randint

computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número entre 0 e 10.')
print('Sera que você consegue adivinhar qual foi?')
acertou = False
palpites = 0

while not acertou:
  jogador = int(input('Qual é seu palpite? '))
  palpites += 1
  if jogador == computador:
    acertou = True
  else:
    if jogador < computador:
      print('Mais... Tente mais uma vez.')
    elif jogador > computador:
      print('Menos... Tente mais uma vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')
