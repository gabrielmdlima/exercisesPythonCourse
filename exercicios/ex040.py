from utils.utils import title, activity
title()
activity('Cálculo da média v2')

score_amount = int(input('Quantas notas são? '))
score = [float(input(f'Digite a {i+1}ª nota: ')) for i in range(score_amount)]
total = 0
for i in range(len(score)):
  total += score[i]
average = total / score_amount
# print(f'A média das notas é {average:.1f}')

if average < 5:
  print(f'Sua média foi {average:.1f} e você está \033[31mREPROVADO!\033[m')
elif 5 <= average < 7:
  print(f'Sua média foi {average:.1f} e você está de \033[33mRECUPERAÇÃO!\033[m')
else:
  print(f'Sua média foi {average:.1f} e você está \033[32mAPROVADO!\033[m PARABÉNS!')
