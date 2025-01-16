from utils.utils import title, activity
title()
activity('Verificação de entrada')

cond = 0
while cond == 0:
  gender = str(input('Digite o sexo [M/F]: ')).strip().upper()
  if gender == 'M' or gender == 'F':
    cond = 1
  else:
    print('Valor inválido, tente M ou F.\n')

print(f'O gênero digitado foi {gender}')

#  Correção do exercício
title()
activity('Correção do exercício')

sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MF':
  sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso.')
