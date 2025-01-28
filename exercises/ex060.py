from utils.utils import title, activity
title()
activity('Fatorial')

num = int(input('Digite um valor: '))
multi = num
count = num

if num == 0:
  multi = '0! = 1'
else:
  print(f'{num}! =', end=' ')
  while count >= 1:
    print(f'{count} =' if count == 1 else f'{count} x', end=' ')
    count -= 1
    if count > 0:
      multi *= count
print(multi)
