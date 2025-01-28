n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print(f'A soma de {n1} com {n2} é {a}, \n a subtração é {s}, \n o produto é {m} e a divisão é {d:.3f}', end=' ')
print(f'A divisão inteira é {di} e a exponenciação de {n1} elevado à {n2} é {e}')
