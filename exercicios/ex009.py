from utils.utils import title, activity
title()
activity('TABUADA')

n = int(input('Digite um número: '))
i = 1
print(f'\nTabuada do {n:2}')
print('='*13)
while i <= 10:
  print(f'{n:2} x {i:2} = {n * i:2}')
  i += 1
print('='*13)
