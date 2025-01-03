from utils.utils import title, activity
title()
activity('Triângulo é possível?')

s = [float(input(f'Digite a {i+1}ª reta: ')) for i in range(3)]

if s[0] < s[1] + s[2] and s[1] < s[0] + s[2] and s[2] < s[0] + s[1]:
  print('Os segmentos acima PODEM formar um trinângulo!')
else:
  print('Os segmementos acima NÃO PODEM formar um triângulo!')
