from utils.utils import title, activity
title()
activity('Listas compostas')

pessoas = list()
dado = list()

while True:
  dado.append(str(input('Nome: ')))
  dado.append(float(input('Peso: ')))
  if len(pessoas) < 1:
    maior = menor = dado[1]
  else:
    if maior < dado[1]:
      maior = dado[1]
    elif menor > dado[1]:
      menor = dado[1]
  pessoas.append(dado[:])
  dado.clear()
  while True:
    stay = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if stay in 'SN':
      break
  if stay == 'N':
    break

print('-='*30)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de', end=' ')
for p in pessoas:
  if p[1] == maior:
    print(f'[{p[0]}]', end=' ')
print()
print(f'O menor peso foi de {menor}Kg. Peso de', end=' ')
for p in pessoas:
  if p[1] == menor:
    print(f'[{p[0]}]', end=' ')
print()
