from utils.utils import title, activity
title()
activity('Análise de cadastros')

nome = [''] *4
idades = [0] *4
genero = [''] *4

total = 0
mais_velho = ''
maior_idade = 0
mulheres = 0

for i in range(4):
  print(f'{i+1}ª pessoa:')
  nome[i] = str(input('Qual o seu nome? ')).strip()
  idades[i] = int(input('Qual a sua idade? '))
  genero[i] = str(input('Qual o seu gênero (M/F)? ')).upper().strip()
  print()
  total += idades[i]
  if genero[i] == 'M' and idades[i] > maior_idade:
    maior_idade = idades[i]
    mais_velho = nome[i]
  elif genero[i] == 'F'and idades[i] < 20:
    mulheres += 1

media = total / 4

print(f'A média da idade das 4 pessoa é {media:.2f}')
print(f'O homem mais velho é o {mais_velho}')
print(f'A quantidade de mulheres abaixo de 20 anos é {mulheres}')
