from utils.utils import title, activity
title()
activity('Análise de tupla')

numbers = (int(input('Digite um número: ')), 
           int(input('Digite outro número: ')), 
           int(input('Digite mais um número: ')), 
           int(input('Digite o último número: ')))

print(f'Você digitou os valores {numbers}')
print(f'O valor 9 apareceu {numbers.count(9)}', 'vezes' if not numbers.count(9) == 1 else 'vez')
if not 3 in numbers:
  print(f'O valor 3 não foi digitado em nenhuma posição')
else:
  print(f'O valor 3 apareceu na {numbers.index(3)+1}ª posição')
print(f'Os valores pares digitados foram', end=' ')
for par in numbers:
  if par % 2 == 0:
    print(par, end=' ')
