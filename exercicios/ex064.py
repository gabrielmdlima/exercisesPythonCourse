from utils.utils import title, activity
title()
activity('Contagem de números')

c = 0
sum = 0
n = 0

while n != 999:
  n = int(input(f'{c+1:2}º número [999 para SAIR]: '))
  if not n == 999:
    sum += n
    c += 1

print(f'Você digitou {c} números e a soma de todos é {sum}.')
