from utils.utils import title, activity
title()
activity('O nome tem "Silva"?')

name = str(input('Digite seu nome completo: ')).strip().upper()
print(f'O nome digitado tem "Silva? {"SILVA" in name}')
