from utils.utils import title, activity
title()
activity('Sequência de Fibonacci')

n = int(input('Quantos números gostaria de mostrar: '))
p = 0
s = 1
print(f'\n0 → 1 → ', end='')

while n > 2:
  value = p + s
  p = s
  s = value
  print(f'{value}' if n == 3 else f'{value} →', end=' ')
  n -= 1
