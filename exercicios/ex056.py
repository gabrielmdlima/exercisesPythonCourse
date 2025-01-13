from utils.utils import title, activity
title()
activity('Análise de cadastros')

total = 0
mais_velho = ''
maior_idade = 0
mulheres = 0

for i in range(4):
  print(f'{i+1}ª pessoa:')
  nome = str(input('Qual o seu nome? ')).strip()
  idade = int(input('Qual a sua idade? '))
  genero = str(input('Qual o seu gênero (M/F)? ')).upper().strip()
  print()
  total += idade
  if genero == 'M' and idade > maior_idade:
    maior_idade = idade
    mais_velho = nome
  elif genero == 'F'and idade < 20:
    mulheres += 1

media = total / 4

print(f'A média da idade das 4 pessoa é {media:.2f}')
print(f'O homem mais velho é o {mais_velho}')
print(f'A quantidade de mulheres abaixo de 20 anos é {mulheres}')
