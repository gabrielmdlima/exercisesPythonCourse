from utils.utils import title, activity
title()
activity('Primeiro e último nome')

name = str(input('Digite seu nome completo: ')).strip().split()
print(f'Seu primeiro nome é: {name[0]}')
print(f'Seu último nome é: {name[-1]}')
print(f'Seu último nome é: {name[len(name) - 1]}')
