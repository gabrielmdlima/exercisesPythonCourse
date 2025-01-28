from utils.utils import title, activity
title()
activity('Real x Dólar')

real = float(input('Quanto dinheiro você tem? R$'))
cotacao = float(input('Qual a cotação atual do dólar? R$'))
dolar = real / cotacao
print(f'Com R${real:.2f} você compra U${dolar:.2f}')
