from utils.utils import title, activity
title()
activity('Classificação de atletas')

from datetime import date

CURRENT_YEAR = date.today().year
YES = ['SIM', 'S', 'YES']
NO = ['NÃO', 'N', 'NO']


def get_age():
  while True:
    birth_date = str(input('Digite sua data de nascimento (DD/MM/YYYY): ')).strip()
    birth_year = int(birth_date.split('/')[-1])
    if birth_year < CURRENT_YEAR:
      age = CURRENT_YEAR - birth_year
      print(f'\nVocê tem {age} anos')
      return age
    elif birth_year > CURRENT_YEAR:
      print(f'\nA data de nascimento não pode ser maior que {CURRENT_YEAR}. Tente novamente.')
    else:
      print(f'\nA data de nascimento não pode ser igual à {CURRENT_YEAR}. Tente novamente.')


def determine_category(age):
  if age <= 9:
    return 'MIRIM'
  elif age <= 14:
    return 'INFANTIL'
  elif age <= 19:
    return 'JUNIOR'
  elif age <= 25:
    return 'SÊNIOR'
  else:
    return 'MASTER'


def yes_or_no(prompt):
  while True:
    choice = str(input(prompt)).upper().strip()
    if choice in YES or choice in NO:
      return choice
    else:
      print('\nResposta inválida! Tente "Sim" ou "Não"')


def classify_athlete():
  print('=' * 32)
  print('CONFEDERAÇÃO NACIONAL DE NATAÇÃO')
  print('=' * 32)
  if yes_or_no('\nVocê gostaria de se matricular na Confederação Nacional de Natação?\n(Sim/Não): ') in NO:
    print('\nObrigado por visitar nosso sistema! Tenha um bom dia!')
    return
  print('\nPrimeiro:')
  
  age = get_age()
  category = determine_category(age)

  print(f'Sua categoria é: {category}')
  print('\nObrigado por usar nosso sistema! Até logo!')

classify_athlete()
