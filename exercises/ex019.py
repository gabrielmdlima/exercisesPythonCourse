from utils.utils import title, activity
title()
activity('Sorteio de alunos')

from random import choice

quantidade = int(input('Quantos alunos tem? '))

lista = [None] * quantidade
for i in range(len(lista)):
  lista[i] = str(input(f'Digite o nome do {i+1}º aluno: '))
print(f'\nDos {len(lista)} alunos, o sortedado foi: {choice(lista)}')
