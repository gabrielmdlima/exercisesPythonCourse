from utils.utils import title, activity
title()
activity('Cálculo do Sen, Cos e Tan')
from math import sin, cos, tan, radians

angulo = float(input('Digite o ângulo que você deseja: '))
sin = sin(radians(angulo))
print(f'O SENO de {angulo}º é {sin:.2f}')
cos = cos(radians(angulo))
print(f'O COSSENO de {angulo}º é {cos:.2f}')
tan = tan(radians(angulo))
print(f'A TANGENTE de {angulo}º é {tan:.2f}')
