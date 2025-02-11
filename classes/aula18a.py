teste = list()

teste.append('Gabriel')
teste.append(22)
galera = list()
galera.append(teste[:])
teste[0] = 'Gustavo'
teste[1] = 40
galera.append(teste[:])
print(galera)
print()  # Pular linha na exibição do console

pessoas = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(pessoas)
print()  # Pular linha na exibição do console

print(pessoas[0])
print()  # Pular linha na exibição do console

print(pessoas[0][0])
print()  # Pular linha na exibição do console

print(pessoas[2][1])
print()  # Pular linha na exibição do console

for p in pessoas:
  print(f'{p[0]} tem {p[1]} anos de idade.')
print()  # Pular linha na exibição do console

pessoal = list()
dado = list()

for c in range(0,3):
  dado.append(str(input('Nome: ')))
  dado.append(int(input('Idade: ')))
  pessoal.append(dado[:])
  dado.clear()
print()  # Pular linha na exibição do console
print(pessoal)
print()  # Pular linha na exibição do console

totmai = totmen = 0
for p in pessoal:
  if p[1] >= 21:
    print(f'{p[0]} é maior de idade.')
    totmai += 1
  else:
    print(f'{p[0]} é menor de idade.')
    totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')

print()  # Pular linha na exibição do console
