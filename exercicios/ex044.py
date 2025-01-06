from utils.utils import title, activity, clear_screen
title()
activity('Condições de pagamento')

import keyboard

OPTIONS = ['\033[32mÀ vista no dinheiro/cheque\033[m', 
           '\033[32mÀ vista no cartão\033[m', 
           '\033[32mAté 2x no cartão\033[m', 
           '\033[32mAté 3x ou mais no cartão\033[m']
price = None
new_price = None
condition = None


def code_label():
  title()
  activity('Condições de pagamento')


def get_price():
  global price
  while True:
    price = float(input('Qual o valor do produto? R$'))
    if price <= 0:
      print('Insira um valor válido superior à R$0.00.\n')
    else:
      return


def print_menu(selected):
  code_label()
  print(f'\033[33mValor do produto:\033[m \033[1mR${price:.2f}\033[m\n')
  print('=== Selecione a condição ===')
  for i, option in enumerate(OPTIONS):
    if i == selected:
      print(f'> {option}')
    else:
      print(f'  {option}')
  print('='*28)
  print('Pressione \033[1mesc\033[m para \033[1mSAIR\033[m.')


def payment_conditions():
  selected = 0
  print_menu(selected)
  
  while True:
    event = keyboard.read_event(suppress = True)
    if event.event_type == 'down':
      if event.name == 'up':
        selected = (selected - 1) % len(OPTIONS)
        print_menu(selected)
      elif event.name == 'down':
        selected = (selected + 1) % len(OPTIONS)
        print_menu(selected)
      elif event.name == 'enter':
        return OPTIONS[selected]
      elif event.name == 'esc':
        return ''


def return_menu(installments, ins_value):
  print('\nPressione \033[1mesc\033[m para \033[1mVOLTAR\033[m.\nPressione \033[1menter\033[m para \033[1mCONFIRMAR\033[m.')
  while True:
    event = keyboard.read_event(suppress = True)
    if event.event_type == 'down':
      if event.name == 'esc':
        execute_program()
        return
      elif event.name == 'enter':
        code_label()
        print(f'O valor final à ser pago na condição "{condition}" selecionada, ficou \033[1mR${new_price:.2f}\033[m', end='')
        if installments >= 2:
          print(f' e o valor de cada parcela, em {installments}x: \033[1mR${ins_value:.2f}\033[m')
        else:
          print()
        print('\n\033[35mObrigado por usar nosso sistema! Até logo.\033[m')
        return


def execute_program():
  global new_price, condition
  condition = payment_conditions()
  installments = 0
  ins_value = 0
  if condition in OPTIONS:
    code_label()
    print(f'\033[33mValor do produto:\033[m \033[1mR${price:.2f}\033[m\n')
    if condition == OPTIONS[0]:
      print(f'{condition} você tem \033[33m10% de desconto\033[m no valor do produto.')
      new_price = price - (price * 10 / 100)
      print(f'Valor com desconto: \033[1mR${new_price:.2f}\033[m')
    elif condition == OPTIONS[1]:
      print(f'{condition} você tem \033[33m5% de desconto\033[m no valor do produto.')
      new_price = price - (price * 5 / 100)
      print(f'Valor com desconto: \033[1mR${new_price:.2f}\033[m')
    elif condition == OPTIONS[2]:
      print(f'{condition} o valor do produto permanece o mesmo.')
      new_price = price
      installments = 2
      ins_value = new_price / installments
      print(f'Valor do produto: \033[1mR${new_price:.2f}\033[m')
      print(f'Valor de cada parcela em {installments}x: \033[1mR${ins_value:.2f}\033[m')
    else:
      print(f'{condition} o valor do produto tem um \033[33macréscimo de 20%\033[m de juros.')
      new_price = price + (price * 20 / 100)
      while installments < 3:
        installments = int(input('Quantas parcelas? '))
        if installments >= 3:
          ins_value = new_price / installments
          print(f'Valor com juros: \033[1mR${new_price:.2f}\033[m')
          print(f'Valor de cada parcela em {installments}x: \033[1mR${ins_value:.2f}\033[m')
        else:
          print(f'Para 2x ou menos, selecione a opção "{OPTIONS[2]}"!')
    
    return_menu(installments, ins_value)
  
  return


if __name__ == '__main__':
  get_price()
  execute_program()
