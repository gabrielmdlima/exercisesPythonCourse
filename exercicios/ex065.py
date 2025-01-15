from utils.utils import title, activity
title()
activity('Média de números')

c = 0
t = 0
sc = 1

while sc == 1:
  x = 0
  n = int(input('Digite um número: '))
  if c == 0:
    bigger = lower = n
  if n > bigger:
    bigger = n
  elif n < lower:
    lower = n
  t += n
  c += 1
  while x == 0:
    again = str(input('Continuar? [S/N]: ')).strip()
    if again == 'S':
      x = 1
    elif again == 'N':
      sc = 0
      x = 1
    else:
      print('Opção inválida. Tente "S" ou "N".')

average = t / c
print(f'\nA média dos {c} números digitados é {average:.1f}')
print(f'O maior número digitado foi {bigger} e o menor foi {lower}')
