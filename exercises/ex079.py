from utils.utils import title, activity
title()
activity('Verificação de entrada')

num = list()

while True:
  n = int(input('Digite um valor: '))
  if n in num:
    print('Valor duplicado! Não vou adicionar...')
  else:
    print('Valor adicionado com sucesso...')
    num.append(n)

  while True:
    stay = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if stay in 'SN':
      break
  if stay == 'N':
    break

print('-='*30)
num.sort()
print(f'Você digitou os valores {num}')
