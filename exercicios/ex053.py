from utils.utils import title, activity
title()
activity('Palíndromo')

phrase = str(input('Digite um frase: ')).strip().replace(' ', '').upper()
lenght = len(phrase) - 1
c = 0
for i in range(len(phrase)):
  if phrase[i] == phrase[lenght]:
    c += 1
  lenght -= 1

if c == len(phrase):
  print(f'A frase É UM PALÍNDROMO!')
else:
  print('A frase NÃO É UM PALÍNDROMO!')
