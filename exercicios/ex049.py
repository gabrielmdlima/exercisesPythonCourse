from utils.utils import title, activity
title()
activity('Tabuada (de novo)')

num = int(input('Digite um número: '))

print(f'\n* TABUADA DO {num} *')
for i in range(1, 11):
  print(f'  {num:2} x {i:2} = {i * num:2}')
print('*'*16)
