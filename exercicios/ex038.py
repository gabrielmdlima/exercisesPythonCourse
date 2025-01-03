from utils.utils import title, activity
title()
activity('Comparação de dois números')

n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
  print(f'O primeiro valor é maior')
elif n2 > n1:
  print(f'O segundo valor é maior')
else:
  print(f'Os valores são iguais')
