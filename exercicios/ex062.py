from utils.utils import title, activity
title()
activity('PA com while melhorado')

f = int(input('Qual o primeiro número: '))
d = int(input('Qual a razão da PA: '))
t = 10

while t != 0:
  while t > 0:
    if t == 1:
      print(f'{f}')
    else:
      print(f'{f}', end=', ')
      f += d
    t -= 1
  t = int(input('Mostrar mais quantos: '))
  f += d
