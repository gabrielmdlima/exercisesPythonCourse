from utils.utils import title, activity
title()
activity('Análise de variável')

var = input('Digite algo: ')
print(f'O tipo primitivo de {var} é {type(var)}')
print(f'{var} é númerico? {var.isnumeric()}')
print(f'{var} é alfabético? {var.isalpha()}')
print(f'{var} é alfanumérico? {var.isalnum()}')
print(f'{var} é um digito? {var.isdigit()}')
print(f'{var} é um espaço? {var.isspace()}')
print(f'{var} está em maiúscula? {var.isupper()}')
print(f'{var} está em minúscula? {var.islower()}')
print(f'{var} tem a primeira letra maiúscula (Capitalizada)? {var.istitle()}')
