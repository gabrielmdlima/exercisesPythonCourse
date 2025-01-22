from utils.utils import title, activity
title()
activity('Sistema de loja')

print('-'*35)
print(f'{"LOJA SUPER BARATÃO":^35}')
print('-'*35)

total = 0
more_than = 0
cheaper = 0
name_cheaper = ''

while True:
  name = str(input('Nome do Produto: '))
  price = float(input('Preço: R$'))
  if not total == 0:
    if price < cheaper:
      name_cheaper = name
      cheaper = price
  else:
    name_cheaper = name
    cheaper = price
  if price >= 1000:
    more_than += 1
  total += price
  while True:
    stay = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if stay in 'SN':
      break
  if stay == 'N':
    print(f'{" FIM DO PROGRAMA ":-^40}')
    break
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {more_than} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {name_cheaper} que custa R${cheaper:.2f}')
