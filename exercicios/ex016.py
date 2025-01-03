from utils.utils import title, activity
from math import trunc
title()
activity('Porção inteira de número real')

num = float(input('Digite um número: '))
print(f'A porção inteira de {num} é {trunc(num)}')
