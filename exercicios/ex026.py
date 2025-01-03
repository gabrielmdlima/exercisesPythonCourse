from utils.utils import title, activity
title()
activity('Encontrando a letra "A"')

word = str(input('Digite uma palavra: ')).strip().upper()
print(f'A letra "a" aparece {word.count("A")}x')
print(f'A primeira aparição é na {word.find("A") + 1}ª posição')
print(f'A útlima apariação é na {word.rfind("A") + 1}ª posição')
