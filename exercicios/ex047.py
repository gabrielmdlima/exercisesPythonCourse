from utils.utils import title, activity
title()
activity('Todos os pares no intervalo')

def even_number(first, last):
  for num in range(first, (last+1)):
    if num % 2 == 0:
      if num == last - 1 or num == last:
        print(num)
      else:
        print(f'{num}, ', end='')


def get_entrance():
  print('Escolha o intervalo\n')
  lista = [0, 0]
  for i in range(2):
    lista[i] = int(input('Primeiro número: ' if i == 0 else 'Último número  : '))
  return lista


def run():
  range = get_entrance()
  f = range[0]
  l = range[1]
  print(f'\nTodos os número pares no intervalo de {f} até {l} são:')
  even_number(f, l)


if __name__ == '__main__':
  run()
