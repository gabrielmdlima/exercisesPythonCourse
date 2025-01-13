from utils.utils import title, activity
title()
activity('Verificação de entrada')

cond = 0
while cond == 0:
  gender = str(input('Digite o sexo: [M/F] '))
  if gender == 'M' or gender == 'F':
    cond = 1
  else:
    print('Valor inválido, tente M ou F.\n')

print(f'O gênero digitado foi {gender}')