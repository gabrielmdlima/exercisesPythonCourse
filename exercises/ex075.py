from utils.utils import title, activity
title()
activity('Análise de tupla')

a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o último número: '))
tupla = (a, b, c, d)

print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)}', 'vezes' if not tupla.count(9) == 1 else 'vez')
if not 3 in tupla:
  print(f'O valor 3 não foi digitado em nenhuma posição')
else:
  print(f'O valor 3 apareceu na {tupla.index(3)+1}ª posição')
print(f'Os valores pares digitados foram', end=' ')
for par in tupla:
  if par % 2 == 0:
    print(par, end=' ')
