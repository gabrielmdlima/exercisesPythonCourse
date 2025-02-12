pessoas = {'nome': 'Gabriel', 'sexo': 'M', 'idade': 22}

print(pessoas)

print()  # Pular linha na exibição do console
print(pessoas['nome'])
print(pessoas['idade'])

print()  # Pular linha na exibição do console
print(f"O {pessoas['nome']} tem {pessoas['idade']} anos.")

print()  # Pular linha na exibição do console
print(pessoas.keys())

print()  # Pular linha na exibição do console
print(pessoas.values())

print()  # Pular linha na exibição do console
print(pessoas.items())

print()  # Pular linha na exibição do console
for k in pessoas.keys():
  print(k)

print()  # Pular linha na exibição do console
for v in pessoas.values():
  print(v)

print()  # Pular linha na exibição do console
for k, v in pessoas.items():
  print(f'{k}: {v}')

print()  # Pular linha na exibição do console
pessoas['nome'] = 'Matheus'
print("\033[33mpessoas['nome'] = 'Matheus'\033[m")
for k, v in pessoas.items():
  print(f'{k}: {v}')

print()  # Pular linha na exibição do console
pessoas['peso'] = 73.4
print("\033[32mpessoas['peso'] = 73.4\033[m")
for k, v in pessoas.items():
  print(f'{k}: {v}')

print()  # Pular linha na exibição do console
del pessoas['sexo']
print("\033[31mdel pessoas['sexo']\033[m")
for k, v in pessoas.items():
  print(f'{k}: {v}')

print()  # Pular linha na exibição do console
brasil = list()
estado1 = {'uf': 'São Paulo', 'sigla': 'SP'}
estado2 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
brasil.append(estado1)
brasil.append(estado2)

print(f'Estado 1: {estado1}')
print()  # Pular linha na exibição do console
print(f'Estado 2: {estado2}')
print()  # Pular linha na exibição do console
print(brasil)

print()  # Pular linha na exibição do console
print(brasil[0])

print()  # Pular linha na exibição do console
print(brasil[0]['uf'])
print(brasil[1]['sigla'])

print()  # Pular linha na exibição do console
estado = dict()
pais = list()

for c in range(3):
  estado['uf'] = str(input('Unidade Federativa: ')).strip()
  estado['sigla'] = str(input('Sigla do Estado: ')).strip()
  pais.append(estado.copy())

for est in pais:
  for v in est.values():
    print(f'{v}' if v == est['sigla'] else f'{v}, ', end='')
  print()

print()  # Pular linha na exibição do console
