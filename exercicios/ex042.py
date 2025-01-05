from utils.utils import title, activity
title()
activity('Análise de trinângulos')

s = [float(input(f'Digite o valor do {i+1}º segmento: ')) for i in range(3)]

if s[0] < s[1] + s[2] and s[1] < s[0] + s[2] and s[2] < s[0] + s[1]:
  if s[0] == s[1] and s[0] == s[2]:
    print(f'\nOs segmentos de reta acima formam um triângulo EQUILÁTERO!')
  elif s[0] == s[1] or s[1] == s[2] or s[2] == s[0]:
    print(f'\nOs segmentos de reta acima formam um triângulo ISÓSCELES!')
  else:
    print(f'\nOs segmentos de reta acima formam um triângulo ESCALENO!')
else:
  print('Os segmementos acima NÃO PODEM formar um triângulo!')
