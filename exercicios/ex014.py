from utils.utils import title, activity
title()
activity('ºC para ºF')

c = float(input('Digite a temperatura em ºC: '))
f = c * 9 / 5 + 32
print(f'A temperatura {c}ºC equivale à {f:.1f}ºF')
