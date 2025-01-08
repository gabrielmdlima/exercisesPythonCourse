from utils.utils import title, activity
title()
activity('Contagem regressiva')

from emoji import emojize
from time import sleep

def countdown():
  for c in range(10, 0, -1):
    print(f'\r{" "*3}', end='')
    print(f'\r{c:2}', end='')
    sleep(1)

def countdown_string():
  num = ('DEZ', 'NOVE', 'OITO', 'SETE', 'SEIS', 'CINCO', 'QUATRO', 'TRÊS', 'DOIS', 'UM')
  for i in range(10):
    print(f'\r{" "*7}', end='')
    print(f'\r{num[i]:^33}', end='')
    sleep(1)

def run():
  countdown_string()
  print(emojize('\r      :sparkles: \033[32mFELIZ ANO NOVO!\033[m :sparkles:'))

if __name__ == '__main__':
  run()
