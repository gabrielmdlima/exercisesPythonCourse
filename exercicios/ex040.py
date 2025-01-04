from utils.utils import title, activity
from datetime import date

# Constantes
MALE = 'M'
FEMALE = 'F'
YES = 'S'
NO = 'N'
REQUIRED_AGE = 18

# Função para exibir título e atividade
title()
activity('Alistamento Militar')

# Função para calcular a idade e determinar a situação do alistamento
def age_verify(birth_year):
    current_year = date.today().year
    age = current_year - birth_year

    if age < REQUIRED_AGE:
        print(f'\nAinda faltam {REQUIRED_AGE - age} anos. Você deve se alistar em {birth_year + REQUIRED_AGE}.')
    elif age == REQUIRED_AGE:
        print('\nVocê deve se alistar este ano.')
    else:
        print(f'\nJá se passaram {age - REQUIRED_AGE} anos. Você deveria ter se alistado em {birth_year + REQUIRED_AGE}.')

# Função para validar entrada de ano de nascimento
def get_birth_year():
    while True:
        try:
            birth_date = input('\nQual sua data de nascimento? (DD/MM/AAAA) ').strip()
            birth_year = int(birth_date.split('/')[-1])
            if birth_year > date.today().year:
                raise ValueError('O ano de nascimento não pode ser no futuro.')
            return birth_year
        except (ValueError, IndexError):
            print('\nEntrada inválida! Certifique-se de inserir a data no formato DD/MM/AAAA.')

# Função principal para verificar o sexo e a decisão do usuário
def enlistment():
    while True:
        gender = input('Qual o seu sexo? (M/F) -> ').strip().upper()
        if gender == FEMALE:
            print('\nVocê não é obrigada a se alistar!')
            while True:
                forward = input('\nGostaria de se alistar mesmo assim? (S/N) -> ').strip().upper()
                if forward == NO:
                    print('Tenha um bom dia!')
                    return
                elif forward == YES:
                    birth_year = get_birth_year()
                    age_verify(birth_year)
                    return
                else:
                    print('\nResposta inválida! Tente novamente.')
        elif gender == MALE:
            while True:
                already = input('\nVocê já se alistou? (S/N) -> ').strip().upper()
                if already == YES:
                    print('\nObrigado por cumprir o seu dever!')
                    return
                elif already == NO:
                    birth_year = get_birth_year()
                    age_verify(birth_year)
                    return
                else:
                    print('\nResposta inválida! Tente novamente.')
        else:
            print('\nResposta inválida! Tente novamente.')

# Início do programa
enlistment()
