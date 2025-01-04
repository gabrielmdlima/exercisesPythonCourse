from utils.utils import title, activity
title()
activity('Alistamento Militar')
from datetime import date

NO = ['N', 'NÃO', 'NO']
YES = ['S', 'SIM', 'YES']
MALE = ['M', 'MASCULINO', 'MACHO', 'HOMEM']
FEMALE = ['F', 'FEMININO', 'FÊMEA', 'MULHER']
CURRENT_YEAR = date.today().year
REQUIRED_AGE = int(18)


def age_verify(birth_year, age):
  if age == 17:
    print(f'\nAinda falta {REQUIRED_AGE - age} ano. Você deve se alistar em {REQUIRED_AGE + birth_year}.')
  elif age == 19:
    print(f'\nJá passou {age - REQUIRED_AGE} ano. Você deveria ter se alistado em {REQUIRED_AGE + birth_year}.')
  elif age < REQUIRED_AGE:
    print(f'\nAinda faltam {REQUIRED_AGE - age} anos. Você deve se alistar em {REQUIRED_AGE + birth_year}.')
  elif age == REQUIRED_AGE:
    print(f'\nVocê deve se alistar esse ano.')
  else:
    print(f'\nJá se passaram {age - REQUIRED_AGE} anos. Você deveria ter se alistado em {REQUIRED_AGE + birth_year}.')


def get_birth_year():
  while True:
    birth_date = str(input('Que dia você nasceu? (DD/MM/YYYY) ')).strip()
    birth_year = int(birth_date.split('/')[-1])
    if birth_year < CURRENT_YEAR:
      age = CURRENT_YEAR - birth_year
      print(f'\nVocê tem {age} anos de idade.')
      return birth_year, age
    elif birth_year >= CURRENT_YEAR:
        print('\nO ano de nascimento não pode ser no futuro.')
    else:
      print('Resposta inválida! Tente novamente.')


def yes_or_no(prompt):
  while True:
    answer = str(input(prompt)).strip().upper()
    if answer in YES or answer in NO:
      return answer
    print('Resposta inválida! Tente "Sim" ou "Não".')


def enlistment():
  while True:
    gender = str(input('Qual o seu gênero? -> ')).strip().upper()
    if gender in FEMALE:
      print('\nVocê não é obrigada a se alistar!')
      if yes_or_no('\nGostaria de se alistar mesmo assim? -> ') in NO:
        print('\nTenha um bom dia!')
        return
      birth_year, age = get_birth_year()
      age_verify(birth_year, age)
      return
    elif gender in MALE:
      birth_year, age = get_birth_year()
      if age >= REQUIRED_AGE:
        if yes_or_no('\nVocê já se alistou? -> ') in YES:
          print('\nObrigado por cumprir o seu dever!')
          return
      age_verify(birth_year, age)
      return
    else:
      print('\nResposta inválida! Tente "M" ou "F".')

enlistment()
