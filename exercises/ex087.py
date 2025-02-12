from utils.utils import title, activity
title()
activity('Matriz v2')

matriz = [[], [], []]

for x in range(3):
  for y in range(3):
    matriz[x].append(int(input(f'Digite um valor para [{x}, {y}]: ')))

pares = 0
tercol = 0
maiseg = max(matriz[1])

print('-='*30)
for linhas in matriz:
  for nums in linhas:
    if nums % 2 == 0:
      pares += nums
    print(f'[{nums:^5}]', end='')
  print()
  tercol += linhas[2]

print('-='*30)

print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {tercol}.')
print(f'O maior valor da segunda linha é {maiseg}.')
