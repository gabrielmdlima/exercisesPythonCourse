from utils.utils import title, activity
title()
activity('Progressão Aritmética')


def get_input():
  list = [0, 0]
  for i in range(2):
    list[i] = int(input('Qual o primeiro número: ' if i == 0 else 'Qual a razão da PA: '))
  
  return list


def print_pa(f, d):
  print('\nPrimeiros 10 valores da PA: ')
  for i in range(10):
    value = f + i * d
    print(f'{value}' if i == 9 else f'{value}, ',end='')


def run():
  pa = get_input()
  first_num = pa[0]
  common_diff = pa[1]
  print_pa(first_num, common_diff)


if __name__ == '__main__':
  run()

  input('\n\nPressione "Enter"...')
  title()
  activity('Correção ex051')

  p = int(input('Primeiro termo: '))
  r = int(input('Razão da progressão: '))
  q = (p + (10 - 1) * r) + r

  for i in range(p, q, r):
    print(f'{i}', end=", ")
  print('ACABOU')