from utils.utils import title, activity
title()
activity('Soma de ímpares multip. 3')

s = 0
for i in range(1, 501):
  if not i % 2 == 0 and i % 3 == 0:
    s += i

print(f'A soma de todos os ímpares múltiplos de 3 é {s}')