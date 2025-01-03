from utils.utils import title, activity
title()
activity('Análise de empréstimo')

house_value = float(input('Qual o valor do imóvel? R$'))
wage = float(input('Qual o salário do comprador? R$'))
years = int(input('Em quantas anos pretende pagar? '))
installments = house_value / (years * 12)

print(f'Em {years} anos, o valor das parcelas será R${installments:.2f}')
if installments > wage * 30 / 100:
  print(f'\033[31mEMPRÉSTIMO NEGADO!\033[m\nO valor da parcela é maior que 30% do salário.')
else:
  print(f'\033[32mEMPRÉSTIMO APROVADO!\033[m')
