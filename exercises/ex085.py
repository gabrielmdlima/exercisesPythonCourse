from utils.utils import title, activity
title()
activity('Listas Pares e Ímpares')

numeros = [[], []]

for i in range(1,8):
  dado = int(input(f'Digite o {i}º valor: '))
  if dado % 2 == 0:
    numeros[0].append(dado)
  else:
    numeros[1].append(dado)

numeros[0].sort()
numeros[1].sort()
print('-='*30)
print(f'Os valores pares digitados foram: {numeros[0]}')
print(f'Os valores ímpares digitados foram: {numeros[1]}')
