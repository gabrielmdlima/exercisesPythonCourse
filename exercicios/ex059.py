from utils.utils import title, activity
title()
activity('Menu com while')

choice = 0

while choice != 5:
  n1 = float(input('Primeiro valor: '))
  n2 = float(input('Segundo valor: '))
  choice = 0
  while choice != 4 and choice != 5:
    print('''
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos números
[5] Sair''')
    choice = int(input('Sua escolha: '))
    if choice == 1:
      sum = n1 + n2
      print(f'\n{n1} + {n2} = {sum}')
    elif choice == 2:
      product = n1 * n2
      print(f'\n{n1} x {n2} = {product}')
    elif choice == 3:
      bigger = n1
      if n2 > bigger:
        bigger = n2
      print(f'\nO maior número entre {n1} e {n2} é {bigger}')
  if not choice == 5:
    print()

print('\nObrigado por usar nosso sistema!')