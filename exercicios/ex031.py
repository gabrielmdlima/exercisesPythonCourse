from utils.utils import title, activity
title()
activity('Cálculo de passagem')

distance = float(input('Qual a distância da viagem? '))
if distance <= 200:
  price = distance * 0.50
else:
  price = distance * 0.45
print(f'O preço da passagem para uma viagem de {distance}km é R${price:.2f}')
