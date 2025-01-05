from utils.utils import title, activity
title()
activity('Cálculo do IMC')


def data_input():
  while True:
    weight = float(input('Qual é o peso? (Em kg): '))
    height = float(input('Qual é a altura? (Em metros): '))
    if weight <= 0:
      print('\nO peso deve ser maior que 0. Tente novamente.')
    elif height <=0:
      print('\nA altura deve ser maior que 0. Tente novamente.')
    else:
      return weight, height


def bmi_classify(bmi):
  if bmi <= 18.5:
    return '\033[33mABAIXO DO PESO\033[m'
  elif 18.5 < bmi <= 25:
    return '\033[32mPESO IDEAL\033[m'
  elif 25 < bmi <= 30:
    return '\033[33mSOBREPESO\033[m'
  elif 30 < bmi <= 40:
    return '\033[31mOBESIDADE\033[m'
  else:
    return '\033[31mOBESIDADE MÓRBIDA\033[m'


def bmi_calculator():
  weight, height = data_input()
  bmi = weight / height ** 2
  return bmi


def main():
  print('='*33)
  print(f'{"CALCULADORA DE IMC":^33}')
  print('='*33)
  print()
  bmi = bmi_calculator()
  print(f'\nSeu IMC: \033[1m{bmi:.2f}\033[m')
  classification = bmi_classify(bmi)
  print(f'Classificação: {classification}!')
  print('\n\033[33mConsulte um médico para uma avaliação mais detalhada, se necessário.\033[m')


if __name__ == '__main__':
  main()
