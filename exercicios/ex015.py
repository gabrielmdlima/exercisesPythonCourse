from utils.utils import title, activity
title()
activity('Aluguel de carro')

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos KMs percorridos? '))
pago = (dias * 60) + (km * 0.15)
print(f'O valor à ser pago é R${pago:.2f}')
