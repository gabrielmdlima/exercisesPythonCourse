from utils.utils import title, activity
title()
activity('Maior e menor da lista')

num = list()
for i in range(5):
  num.append(int(input(f'Digite um valor para a Posição {i}: ')))

print('=-'*30)
print(f'Você digitou os valores {num}')
print(f'O maior valor digitado foi {max(num)} nas posições', end=' ')
for i, n in enumerate(num):
  if n == max(num):
    print(i, end='... ')
print()
print(f'O menor valor digitado foi {min(num)} nas posições', end=' ')
for i, n in enumerate(num):
  if n == min(num):
    print(i, end='... ')
