from utils.utils import title, activity
title()
activity('Números primos')

num = int(input('Digite um número: '))
count = 0
for i in range(1, num+1):
  if num % i == 0:
    count += 1

if count == 2:
  print(f'{num} \033[32mÉ\033[m um número primo')
else:
  print(f'{num} \033[31mNÃO É\033[m número primo')
