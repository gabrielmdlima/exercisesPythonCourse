from utils.utils import title, activity
title()
activity('Números por extenso')

numbers = ('zero', 'um', 'dois', 'três', 'quatro',
          'cinco', 'seis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze', 'catorze',
          'quinze', 'dezesseis', 'dezessete', 'dezoito', 
          'dezenove', 'vinte')

while True:
  while True:
    user_input = int(input('Digite um número entre 0 e 20: '))
    if 0 <= user_input <= 20:
      break
    print('Tente novamente.', end=' ')
  print(f'Você digitou o número {numbers[user_input]}')
  while True:
    stay = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    if stay in 'SN':
      break
    else:
      print('Resposta inválida. Tente novamente!')
  if stay == 'N':
    break
print('\nAté logo!')
