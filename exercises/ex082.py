from utils.utils import title, activity
title()
activity('')

numbers = list()
par = list()
impar = list()

while True:
  numbers.append(int(input('Digite um número: ')))
  while True:
    stay = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if stay in 'SN':
      break
  if stay == 'N':
    break

print('-='*30)
print(f'A lista completa é {numbers}')

for n in numbers:
  if n % 2 == 0:
    par.append(n)
  else:
    impar.append(n)
print(f'A lista de pares é {par}')
print(f'A lista de ímpares é {impar}')
