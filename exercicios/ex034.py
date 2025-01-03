from utils.utils import title, activity
title()
activity('Aumento com base no salário')

wage = float(input('Qual o salário do funcionário? R$'))

if wage <= 1250:
  print(f'O novo salário com 15% de aumento é R${wage + (wage * 15 / 100):.2f}')
else:
  print(f'O novo salário com 10% de aumento é R${wage + (wage * 10 / 100):.2f}')
