from utils.utils import title, activity
title()
activity('Números por extenso')

numbers = ('zero', 'um', 'dois', 'três', 'quatro',
          'cinco', 'seis', 'sete', 'oito', 'nove',
          'dez', 'onze', 'doze', 'treze', 'catorze',
          'quinze', 'dezesseis', 'dezessete', 'dezoito', 
          'dezenove', 'vinte')

user_input = int(input('Digite um número entre 0 e 20: '))
if not 0 <= user_input <= 20:
  while True:
    user_input = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    if 0 <= user_input <= 20:
      break
print(f'Você digitou o número {numbers[user_input]}')
