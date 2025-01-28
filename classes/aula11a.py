print('\033[7;35mOlá, Mundo!\033[m')

a = 3
b = 5
print(f'Os valores são \033[7;30;42m{a}\033[m e \033[7;30;41m{b}\033[m!')

cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'verde': '\033[32m',
         'vermelho': '\033[31m'}

print(f'Os valores são {cores['verde']}{a}{cores['limpa']} e {cores['vermelho']}{b}{cores['limpa']}!')
