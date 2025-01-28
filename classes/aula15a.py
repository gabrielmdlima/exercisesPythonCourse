from os import system
system('cls')

cont = 0
while True:
  cont += 1
  print(cont, end=' -> ')
  if cont == 10:
    break
print('Acabou')

print()
print('='*60)
print()

n = s = 0
while True:
  n  = int(input('Digite um número: '))
  if n == 999:
    break
  s += n
print(f'A soma vale {s}')
