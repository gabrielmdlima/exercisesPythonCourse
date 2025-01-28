# from math import sqrt, floor
import math
num = int(input('Digite um número: '))
# raiz = sqrt(num)
raiz = math.sqrt(num)
# print(f'A raiz de {num} é igual à {floor(raiz)}')
print(f'A raiz quadrada de {num} é igual à {math.ceil(raiz):.2f} arredondada para cima.')
print(f'A raiz quadrada de {num} é igual à {raiz:.2f}.')
print(f'A raiz quadrada de {num} é igual à {math.floor(raiz):.2f} arredondada para baixo.')
