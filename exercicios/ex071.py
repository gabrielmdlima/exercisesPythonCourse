from utils.utils import title, activity
title()
activity('Caixa eletrônico')

print('='*30)
print(f'{"BANCO LIMA":^30}')
print('='*30)

value = int(input('Que valor você quer sacar? R$'))
fifty = twenty = ten = one = 0

while True:
  if value >= 50:
    value -= 50
    fifty += 1
  elif value >= 20:
    value -= 20
    twenty += 1
  elif value >= 10:
    value -= 10
    ten += 1
  elif value >= 1:
    value -= 1
    one += 1
  else:
    break

title()
activity('Caixa eletrônico')

print('='*30)
print(f'{"BANCO LIMA":^30}')
print('='*30)

if fifty > 0:
  print(f'Total de {fifty:2} cédula{"s" if fifty > 1 else ""} de R$50')
if twenty > 0:
  print(f'Total de {twenty:2} cédula{"s" if twenty > 1 else ""} de R$20')
if ten > 0:
  print(f'Total de {ten:2} cédula{"s" if ten > 1 else ""} de R$10')
if one > 0:
  print(f'Total de {one:2} cédula{"s" if one > 1 else ""} de R$1')
print('='*30)
print('Volte sempre ao BANCO LIMA! Tenha um bom dia!')
