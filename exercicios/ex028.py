from utils.utils import title, activity
title()
activity('Advinhe o número')

from random import randint

computer = randint(1, 5)
guess = int(input('Advinhe o número de 1 à 5: '))
print('Parabéns! Você acertou!' if guess == computer else 'Que pena, você errou!')
if guess == computer:
  print('*\\/*')
else:
  print(f'O número era {computer}')
