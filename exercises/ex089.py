from utils.utils import title, activity
title()
activity('Boletim escolar')

boletim = list()
dados = list()
notas = list()

while True:
  dados.append(str(input('Nome: ')).strip())
  for i in range(1,3):
    notas.append(float(input(f'Nota {i}: ')))
  dados.append(notas[:])
  boletim.append(dados[:])
  notas.clear()
  dados.clear()

  while True:
    stay = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if stay in 'SN':
      break
  if stay == 'N':
    break

print('-='*30)

print(f'Nº  NOME         MÉDIA')
print('-'*26)
for n, aluno in enumerate(boletim):
  media = (aluno[1][0] + aluno[1][1]) / 2
  print(f'{n}   {aluno[0]:<10}{media:>7.1f}')
while True:
  print('-'*30)
  select = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
  if select == 999:
    print('FINALIZANDO...')
    break
  if select < len(boletim):
    print(f'Notas de {boletim[select][0]} são {boletim[select][1]}')
print('<<< VOLTE SEMPRE >>>')
