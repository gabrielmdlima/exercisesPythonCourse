n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1+n2)/2
print(f'A sua média foi {m:.1f}')
'''
if m >= 6.0:
  print(f'Sua média foi boa! PARABÉNS!')
else:
  print(f'Sua média foi ruim! ESTUDE MAIS!')
'''
print(f'PARABÉNS!' if m>= 6.0 else f'ESTUDE MAIS!')
