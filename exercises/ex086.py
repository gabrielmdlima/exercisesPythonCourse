from utils.utils import title, activity
title()
activity('Matriz')

matriz = [[], [], []]

for x in range(3):
  for y in range(3):
    matriz[x].append(int(input(f'Digite um valor para [{x}, {y}]: ')))
print('-='*30)

for linhas in matriz:
  for nums in linhas:
    print(f'[{nums:^5}]', end='')
  print()
