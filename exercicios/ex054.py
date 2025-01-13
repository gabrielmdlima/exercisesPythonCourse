from utils.utils import title, activity
title()
activity('Verificação de idade')

from datetime import date

current_year = date.today().year
majority = 0
minority = 0

for i in range(7):
  birth_years = int(input(f'Digite ano de nascimento da {i+1}ª pessoa: '))
  if (current_year - birth_years) >= 21:
    majority += 1
  else:
    minority += 1

print(f'\nA quantidade de pessoas que não atingiu a maioridade é {minority} e que atingiram é {majority}')
