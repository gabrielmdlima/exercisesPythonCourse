from utils.utils import title, activity
title()
activity('A cidade começa com "Santo"?')
city = str(input('Digite o nome da cidade: ')).strip().upper().split()
print(f'A cidade começa com "Santo"? {"SANTO" in city[0]}')
