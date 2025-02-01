num = [2, 5, 9, 1]
print(num)

num[2] = 3  # Troca o item na posição 2 pelo elemento 3.
print(num)

num.append(7)  # Adiciona um elemento 7 ao final da lista.
print(num)
print(num[0])

num.sort()  # Reordena a lista do menor pro maior.
print(num)
print(num[0])

num.sort(reverse=True)  # Reordena a lista do maior pro menor.
print(num)
print(num[0])

print(f'Essa lista tem {len(num)} elementos.')  # Imprime a quantidade de elementos da lista no momento.

num.insert(2, 0)  # Insere um elemento 0 na posição 2, nesse caso.
print(num)
print(f'Essa lista tem {len(num)} elementos.')  # Imprime a quantidade de elementos da lista no momento.

num.pop()  # Remove o último elemento.
print(num)

num.pop(2)  # Remove o elemento na posição 2.
print(num)

num.insert(2, 2)
print(num)
num.remove(2)  # Remove a primeira aparição do elemento especificado.
print(num)

if 4 in num: # O 'in' verifica se o elemento está na lista.
  num.remove(4)
else:
  print('Não achei elemento 4')
print(num)

valores = list(range(3,11)) # Cria uma lista com números de 3 à 10.

for v in valores:  # Percorre a lista, alocando cada elemento em v um de cada vez
  print(f'{v}; ', end='')
print()

valores = []

for i in range(1, 6): # De 1 a 5 irá pegar 5 valores
  valores.append(int(input(f'Digite o {i}º valor: ')))

for i, v in enumerate(valores):
  print(f'Na posição {i} encontrei o valor {v}!')
print('Cheguei ao final da lista.\n')

a = [2, 3, 4, 7]
b = a # Cria uma ligação entre as listas
print(f'Antes da alteração. Lista A: {a}')
b[2] = 8 # Altera o item 2 das duas listas
print('\nDepois da alteração.')
print(f'Lista A: {a}')
print(f'Lista B: {b}')

c = [2, 3, 4, 7]
d = c[:]  # Criando uma cópia de c em d
d[2] = 9
print(f'Lista C: {c}')
print(f'Lista D: {d}')
