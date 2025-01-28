from utils.utils import title, activity
title()
activity('Converção de metros')

m = float(input('Um valor em metros: '))
km = m / 1000
hm = m / 100
dam = m / 10
dm = m * 10
cm = m * 100
mm = m * 1000
print(f'A medida de {m}m corresponde à:'
      f'\n{km}km'
      f'\n{hm}m'
      f'\n{dam}dam'
      f'\n{dm:.0f}dm'
      f'\n{cm:.0f}cm'
      f'\n{mm:.0f}mm')
