from utils.utils import title, activity
title()
activity('Data de nascimento')

print(f'Qual a sua data de nascimento?')
dia = int(input('Dia: '))
mes = input('Mês: ')
ano = int(input('Ano: '))
print(f'Você nasceu dia {dia}/{mes}/{ano}. Correto?')
