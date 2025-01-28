from utils.utils import title, activity
title()
activity('Números aleatórios')

from random import randint

random_numbers = (
  randint(1, 9),
  randint(1, 9),
  randint(1, 9),
  randint(1, 9),
  randint(1, 9))

print('Os valores sorteados foram:', end=' ')
for i, number in enumerate(random_numbers):
  print(f'{number}', end=' ')
print(f'\nO maior valor sorteado foi {max(random_numbers)}')
print(f'O menor valor sorteado foi {min(random_numbers)}')
