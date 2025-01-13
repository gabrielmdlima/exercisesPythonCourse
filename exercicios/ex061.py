from utils.utils import title, activity
title()
activity('Progressão Aritmética While')

f = int(input('Qual o primeiro número: '))
d = int(input('Qual a razão da PA: '))
c = 0

while c < 10:
  value = f + c * d
  print(f'{value}' if c == 9 else f'{value}, ',end='')
  c += 1
