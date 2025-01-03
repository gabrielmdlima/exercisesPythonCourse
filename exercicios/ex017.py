from utils.utils import title, activity
title()
activity('Cálculo do hipotenusa')
from math import hypot

a = float(input('Qual o cateto oposto? '))
b = float(input('Qual o cateto adjacente? '))
c = hypot(a, b)
print(f'A hipotenusa vai medir {c:.2f}')
