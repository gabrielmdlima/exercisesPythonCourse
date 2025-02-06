from utils.utils import title, activity
title()
activity('Ordenar lista sem sort')

num = []

while len(num) < 5:
  number = int(input('Digite um valor: '))

  position = 0
  while position < len(num) and num[position] < number:
    position += 1
  
  if position == len(num):
    num.append(number)
    print('Adicionado ao final da lista...')
  else:
    num.insert(position, number)
    print(f'Adicionado na posição {position} da lista...')

print('-='*30)
print(f'Os valores digitados em ordem foram {num}')
