from utils.utils import title, activity
title()
activity('Análise de cadastros v2')

majority = 0
mens = 0
womens = 0

while True:
  print('-'*25)
  print(f'{"CADASTRE UMA PESSOA":^25}')
  print('-'*25)
  age = int(input('Idade: '))
  while True:
    gender = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if gender in 'MF':
      break
  if age >= 18:
    majority += 1
  if gender == 'M':
    mens += 1
  elif age < 20:
    womens += 1
  print('-'*25)
  while True:
    stay = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if stay in 'SN':
      break
  if stay == 'N':
    print(f'{" FIM DO PROGRAMA ":=^30}')
    break
print(f'Total de pessoas com mais de 18 anos: {majority}')
print(f'Ao todo temos {mens} homens cadastrados')
print(f'E temos {womens} mulheres com menos de 20 anos')
