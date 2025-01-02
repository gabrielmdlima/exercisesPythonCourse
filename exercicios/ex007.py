from utils.utils import title, activity
title()
activity('Cálculo da média')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print(f'A média das notas {n1:.1f} e {n2:.1f} é {m:.1f}')
