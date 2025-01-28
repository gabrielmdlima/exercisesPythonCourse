from os import system
system('cls')

c = 1
while c <= 5:
  print(c)
  c += 1
print('FIM\n')

n = 1
while n != 0:
  n = int(input('Digite um valor: '))
print('FIM\n')

r = 'S'
i = 0
while r == 'S':
  i += 1
  input(f'{i}º valor: ')
  r = str(input('Quer continuar? [S/N] ')).upper()
print('FIM\n')

v = 1
par = impar = 0
while v != 0:
  v = int(input('Digite um valor: '))
  if not v == 0:
    if v % 2 == 0:
      par += 1
    else:
      impar += 1
print(f'Você digitou {par} números pares e {impar} números ímpares.')
