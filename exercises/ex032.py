from utils.utils import title, activity
title()
activity('É ano bissexto?')

year = int(input('Digite o ano: '))
if year % 4 == 0 and year %  100 != 0 or year % 400 == 0:
  print(f'{year} é BISSEXTO!')
else:
  print(f'{year} NÃO é BISSEXTO!')
