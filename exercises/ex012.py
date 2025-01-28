from utils.utils import title, activity
title()
activity('Preço com 5% de desconto')

preço = float(input('Qual o preço do produto? R$'))
novoPreço = preço - preço * 5 / 100
print(f'Desconto de 5% = R${preço * 5 / 100:.2f}')
print(f'Preço com 5% de desconto = R${novoPreço:.2f}')
