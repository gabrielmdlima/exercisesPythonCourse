from utils.utils import title, activity
title()
activity('Maior e menor peso')

for i in range(5):
  weights = float(input(f'Digite o {i+1}º peso (kg): '))
  if i == 0:
    bigest = weights
    lowest = weights
  if weights > bigest:
    bigest = weights
  elif weights < lowest:
    lowest = weights

print(f'\nO menor peso lido foi {lowest:.1f}kg e o maior foi {bigest:.1f}kg')
