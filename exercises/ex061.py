from utils.utils import title, activity
title()
activity('Progressão Aritmética While')

f = int(input('Qual o primeiro número: '))
d = int(input('Qual a razão da PA: '))
t = 10

while t > 0:
  if t == 10:
    print(f'{f}', end=', ')
    f += d
  elif t == 1:
    print(f'{f}')
  else:
    print(f'{f}', end=', ')
    f += d
  t -= 1
