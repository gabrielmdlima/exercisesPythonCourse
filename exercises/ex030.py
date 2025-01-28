from utils.utils import title, activity
title()
activity('Par ou ímpar')

num = int(input('Digite um número: '))
if num % 2 == 0:
  print(f'{num} é um número PAR!')
else:
  print(f'{num} é um número ÍMPAR!')
