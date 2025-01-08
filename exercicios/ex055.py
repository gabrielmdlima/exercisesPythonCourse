from utils.utils import title, activity
title()
activity('Maior e menor peso')

weights = [0] * 5
bigest = 0
lowest = 1000

for i in range(5):
  weights[i] = float(input(f'Digite o {i+1}º peso (kg): '))
  if weights[i] > bigest:
    bigest = weights[i]
  elif weights[i] < lowest:
    lowest = weights[i]

print(f'\nO menor peso lido foi {lowest:.1f}kg e o maior foi {bigest:.1f}kg')