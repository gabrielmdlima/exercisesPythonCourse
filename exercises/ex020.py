from utils.utils import title, activity
title()
activity('Ordem de apresentação: ')

from random import shuffle

quantidade = int(input('Quantos alunos são? '))

lista = [''] * quantidade
for i in range(len(lista)):
  lista[i] = str(input(f'Digite o nome do {i+1}º aluno: '))
print('\nA ordem de apresentação será:')
shuffle(lista)
for nome in lista:
  print(nome)
