from utils.utils import title, activity
title()
activity('Contagem de números v2')

count = 0
sum = 0

while True:
  n = int(input('Digite um valor (999 para parar): '))
  if n == 999:
    break
  sum += n
  count += 1

print(f'A soma dos {count} valores foi {sum}!')
