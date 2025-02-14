from utils.utils import title, activity
title()
activity('Cadastro de pessoas')

pessoas = list()
dados = dict()
total_idade = 0

while True:
  dados['nome'] = str(input('Nome: ')).strip()
  dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
  dados['idade'] = int(input('Idade: '))
  total_idade += dados['idade']
  pessoas.append(dados.copy())

  while True:
    stay = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if stay in 'SN':
      break
  if stay == 'N':
    break
print('-='*30)
print(f'- O grupo tem {len(pessoas)} pessoas.')
media = total_idade / len(pessoas)
print(f'- A média de idade é de {media:.2f} anos.')
print(f'- As mulheres cadastradas foram:', end=' ')
for p in pessoas:
  if p['sexo'] == 'F':
    print(f'{p["nome"]}', end=' ')
print()
print('- Lista das pessoas que estão acima da média:')
for p in pessoas:
  if p['idade'] > media:
    print()
    for k, v in p.items():
      print(f'{k} = {v};', end=' ')
    print()
print('<< ENCERRADO >>')
