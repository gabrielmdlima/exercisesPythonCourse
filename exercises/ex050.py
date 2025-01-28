from utils.utils import title, activity
title()
activity('Soma de números pares')

s = 0
for i in range(6):
  n = int(input(f'{i+1}º número inteiro: '))
  if n % 2 == 0:
    s += n

print(f'A soma dos números pares acima é: {s}')
