from utils.utils import title, activity
title()
activity('Manipulando strings')

name = str(input('Digite seu nome completo: ')).strip()
split = name.split()
print(f'Seu nome em maiúsculas é {name.upper()}')
print(f'Seu nome em minúsculas é {name.lower()}')
print(f'Seu nome tem ao todo {len(name) - name.count(" ")} letras')
print(f'Seu primeiro nome é {split[0]} e ele tem {len(split[0])} letras')
print(f'Seu último nome é {split[-1]} e ele tem {len(split[-1])} letras')
