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
input('\nPRESSIONE ENTER PARA IR PARA A CORREÇÃO...')
title()
activity('CORREÇÃO DO EXERCÍCIO')

lista = []

for c in range(0,5):
  n = int(input('Digite um valor: '))
  if c == 0 or n > lista[-1]:
    lista.append(n)
    print('Adicionado ao final da lista...')
  else:
    pos = 0
    while pos < len(lista):
      if n <= lista[pos]:
        lista.insert(pos, n)
        print(f'Adicionado na posição {pos} da lista...')
        break
      pos += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')
