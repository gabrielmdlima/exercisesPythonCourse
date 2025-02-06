from utils.utils import title, activity
title()
activity('Análise de valores')

num = list()
while True:
  num.append(int(input('Digite um valor: ')))
  while True:
    stay = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if stay in 'SN':
      break
  if stay == 'N':
    break
print('-='*30)
print(f'Você digitou {len(num)} elementos.')

num.sort(reverse=True)
print(f'Os valores em ordem decrescente são {num}')

if 5 in num:
  print('O valor 5 faz parte da lista!')
else:
  print('O valor 5 não foi encontrado na lista!')
