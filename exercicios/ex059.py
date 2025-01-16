from utils.utils import title, activity

choice = 0

while choice != 5:
  title()
  activity('Menu com while')
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
    elif choice > 5 or choice == 0:
      print('\nResposta inválida. Tente novamente!')
  if not choice == 5:
    print()

print('\nObrigado por usar nosso sistema!')

#  Correção do exercício
title()
activity('Correção do exercício')

from time import sleep

x1 = float(input('Primeiro valor: '))
x2 = float(input('Segundo valor: '))
opcao = 0
while opcao != 5:
  print('''  [1] somar
  [2] multiplicar
  [3] maior
  [4] novos números
  [5] sair do programa''')
  opcao = int(input('>> Qual é a sua opção? '))
  if opcao == 1:
    soma = x1 + x2
    print(f'A soma entre {x1} + {x2} é {soma}')
  elif opcao == 2:
    produto = x1 * x2
    print(f'O resultado de {x1} x {x2} é {produto}')
  elif opcao == 3:
    if x1 > x2:
      maior = x1
    else:
      maior = x2
    print(f'Entre {x1} e {x2} o maior valor é {maior}')
  elif opcao == 4:
    print('Informe os números novamente:')
    x1 = float(input('Primeiro valor: '))
    x2 = float(input('Segundo valor: '))
  elif opcao == 5:
    print('Finalizando...')
  else:
    print('Opção inválida. Tente novamente!')
  print('=-=' * 10)
  sleep(2)
print('Fim do programa! Volte Sempre!')