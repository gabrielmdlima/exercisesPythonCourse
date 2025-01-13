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