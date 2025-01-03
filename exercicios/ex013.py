from utils.utils import title, activity
title()
activity('Salário com 15% de aumento')

salario = float(input('Qual o salário do funcionário? R$'))
novoSalario = salario + (salario * 15 / 100)
print(f'Aumento de 15% = R${salario * 15 / 100:.2f}')
print(f'Salário com 15% de aumento = R${novoSalario:.2f} ')
