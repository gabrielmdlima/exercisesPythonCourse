lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita') 
# Tuplas podem ser tanto com ou sem os parênteses. Ex: 'Hambúrguer', 'Suco', 'Pizza', 'Pudim' ou ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
# Tuplas são IMUTÁVEIS
# lanche[1] = 'Refrigerante' -> Este comando está errado, tuplas não podem ser alteradas.

print(lanche)

print(lanche[1])
print(lanche[3])
print(lanche[-2])
print(lanche[1:3])
print(lanche[2:])
print(lanche[:2])
print(lanche[-2:])
print(lanche[-3:])
print(len(lanche))

print()  # Pular linha na exibição do console
for comida in lanche:
  print(f'Comi {comida}')
print('Comi pra caramba!')

print()  # Pular linha na exibição do console
for cont in range(0, len(lanche)): # 0 até tamanho da lista.
  print(f'Comi {lanche[cont]} na posição {cont}')
print('Comi pra caramba!')

print()  # Pular linha na exibição do console
for pos, comida in enumerate(lanche):
  print(f'Comi {comida} na posição {pos}')
print('Comi pra caramba!')

print()  # Pular linha na exibição do console
print(sorted(lanche)) # Coloca os itens em ordem

print()  # Pular linha na exibição do console
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a  # Junta as duas listas, na ordem em que é feita a junção
print(a)
print(b)
print(c)
print(len(c))  # Mostra a quantidade de itens na tupla, nesse caso igual à 7
print(c.count(5))  # Mostra quantas vezes o item '5' aparece na tupla, nesse caso igual à 2
print(c.count(4))  # Mostra quantas vezes o item '4' aparece na tupla, nesse caso igual à 1
print(c.count(9))  # Mostra quantas vezes o item '9' aparece na tupla, nesse caso igual à 0
print(c.index(8))  # Mostra a primeira posição que o item '8' aparace na tupla, nesse caso igual à 1
print(c.index(4))  # Mostra a primeira posição que o item '4' aparace na tupla, nesse caso igual à 6
print(c.index(2))  # Mostra a primeira posição que o item '2' aparace na tupla, nesse caso igual à 3
print(c.index(2, 4))  # Mostra a primeira posição que o item '2' aparece a partir da posição 4, nesse caso igual à 4
print(c.index(5))  # Mostra a primeira posição que o item '5' aparace na tupla, nesse caso igual à 0
print(c.index(5, 1))  # Mostra a primeira posição que o item '5' aparece a partir da posição 1, nesse caso igual à 5

print()  # Pular linha na exibição do console
pessoa = ('Gabriel', 22, 'M', 70.4)  # Tuplas podem receber items de diferentes tipos
print(f"Tupla 'pessoa': {pessoa}")

print()  # Pular linha na exibição do console
try:
  print("del(pessoa[0])  # Tentando deletar o item 0 da tupla 'pessoa'")
  del(pessoa[0])
except TypeError as error:
  print()
  print(f'\033[31mErro: {error}\033[m')
  print('\033[33mNão é possível deletar um único item de uma tupla!\033[m')

print()  # Pular linha na exibição do console
try:
  print("del(pessoa)  # Deletando a tupla 'pessoa' da memória \nprint(pessoa)")
  del(pessoa)  # Única alteração possivel a se fazer na Tupla é deletar ela da memória
  print(pessoa)
except NameError as error:
  print()
  print(f'\033[31mErro: {error}\033[m')
  print("\033[33mTupla 'pessoa' foi deletada!\033[m")
