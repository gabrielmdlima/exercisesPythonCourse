from utils.utils import title, activity
title()
activity('Qual o maior e menor número')

# size = int(input('Qual o tamanho da lista? '))  # Declarar no range do for
num = [int(input(f'Digite o {i+1}º número: ')) for i in range(3)]
bigger = smaller = num[2]
# maior = menor = num[0]

# Comparando quem é maior
if num[0] > num[1] and num[0] > num[2]:
  bigger = num[0]
elif num[1] >= num[0] and num[1] > num[2]:
  bigger = num[1]

# Comparando quem é menor
if num[0] < num[1] and num[0] < num[2]:
  smaller = num[0]
elif num[1] <= num[0] and num[1] < num[2]:
  smaller = num[1]
print(f'O maior número é {bigger} e o menor é {smaller}')


"""for n in num[1:]:
  if n > maior:
    maior = n
  elif n < menor:
    menor = n"""

# print(f'O maior número é {maior} e o menor é {menor}')

