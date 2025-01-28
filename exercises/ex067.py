from utils.utils import title, activity
title()
activity('Tabuada v3')

while True:
  count = 1
  value = int(input('Quer ver a tabuada de qual valor? '))
  print('-'*40)
  if value < 0:
    break
  while True:
    print(f'{value} x {count:2} = {value * count}')
    count += 1
    if not count <= 10:
      break
  print('-'*40)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
