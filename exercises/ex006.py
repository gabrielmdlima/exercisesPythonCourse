from utils.utils import title, activity
from math import sqrt
title()
activity('Dobro, triplo e raiz quadrada')

n = int(input('Digite um número: '))
print(f'O número digitador foi {n}:\nSeu dobro é {n*2}\nSeu triplo é {n*3}\nE sua raiz quadrada é {sqrt(n)}')
