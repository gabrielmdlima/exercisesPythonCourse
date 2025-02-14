from utils.utils import title, activity
title()
activity('Carteira de trabalho')
from datetime import date

C_YEAR = date.today().year

ficha = dict()

ficha['nome'] = str(input('Nome: ')).strip()
while True:
  nascimento = int(input('Ano de Nascimento: '))
  if not nascimento == 0:
    if nascimento < C_YEAR:
      idade = C_YEAR - nascimento
      ficha['idade'] = idade
      break
  print(f'Ano não pode ser 0 ou maior/igual à {C_YEAR}')

ficha['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if ficha['ctps'] > 0:
  ficha['contratação'] = int(input('Ano de contratação: '))
  ficha['salário'] = float(input('Salário: R$'))
  ano_aposentadoria = ficha['contratação'] + 35
  ficha['aposentadoria'] = ano_aposentadoria - nascimento

print('-='*30)
print(ficha)
for k, v in ficha.items():
  print(f'{k} tem o valor {v}')
