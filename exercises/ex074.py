from utils.utils import title, activity
title()
activity('Números aleatórios')

from random import randint

random_numbers = (
  randint(0, 9),
  randint(0, 9),
  randint(0, 9),
  randint(0, 9),
  randint(0, 9))

print('Os valores sorteados foram:', end=' ')
for i, number in enumerate(random_numbers):
  print(f'{number}', end=' ')
  if i == 0:
    bigger = number
    lower = number
  if number > bigger:
    bigger = number
  elif number < lower:
    lower = number
print()
print(f'O maior valor sorteado foi {bigger}')
print(f'O menor valor sorteado foi {lower}')
