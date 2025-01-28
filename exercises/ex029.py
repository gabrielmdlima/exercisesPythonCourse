from utils.utils import title, activity
title()
activity('Radar de velocidade')

speed = float(input('A qual velocidade o carro estava? '))
print()
if speed > 80:
  print(f'\033[31mMULTADO!\033[m \033[33mVocê excedeu o limite permitido de 80 Km/h\033[m')
  print(f'O valor da multa é R${(speed - 80) * 7:.2f}')
else:
  print('\033[32mTenha um bom dia! Dirija com segurança!\033[m')
