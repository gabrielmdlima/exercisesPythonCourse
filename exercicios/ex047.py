from utils.utils import title, activity
title()
activity('Todos os pares no intervalo')

def even_number(first, last):
  for num in range(first, (last+1)):
    if num % 2 == 0 and num != last:
      print(f'{num}, ', end="")
    elif num % 2 == 0:
      print(num)


def get_entrance():
  print('Escolha o intervalo\n')
  lista = [0, 0]
  for i in range(2):
    lista[i] = int(input(f'{i+1}º número: '))
  return lista


def run():
  range = get_entrance()
  f = range[0]
  l = range[1]
  print(f'\nTodos os número pares no intervalo de {f} até {l} são:')
  even_number(f, l)


if __name__ == '__main__':
  run()
