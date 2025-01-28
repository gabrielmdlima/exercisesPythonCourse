from utils.utils import title, activity
title()
activity('Condições de pagamento')

import keyboard

OPTIONS = ('\033[32mÀ vista no dinheiro/cheque\033[m', 
           '\033[32mÀ vista no cartão\033[m', 
           '\033[32mAté 2x no cartão\033[m', 
           '\033[32mAté 3x ou mais no cartão\033[m')


class Variables:
  def __init__(self):
    self.price = 0
    self.new_price = 0
    self.condition = 0
    self.selected = 0
    self.installments = 0
    self.ins_value = 0


def code_label():
  title()
  activity('Condições de pagamento')


def get_price(var):
  while True:
    var.price = float(input('Qual o valor do produto? R$'))
    if var.price <= 0:
      print('Insira um valor válido, superior à R$0.00.\n')
    else:
      return


def print_menu(var):
  code_label()
  print(f'\033[33mValor do produto:\033[m \033[1mR${var.price:.2f}\033[m\n')
  print('=== Selecione a condição ===')
  for i, option in enumerate(OPTIONS):
    if i == var.selected:
      print(f'> {option}')
    else:
      print(f'  {option}')
  print('='*28)
  print('Pressione \033[1mesc\033[m para \033[1mSAIR\033[m.')


def payment_conditions(var):
  print_menu(var)
  
  while True:
    event = keyboard.read_event(suppress = True)
    if event.event_type == 'down':
      if event.name == 'up':
        var.selected = (var.selected - 1) % len(OPTIONS)
        print_menu(var)
      elif event.name == 'down':
        var.selected = (var.selected + 1) % len(OPTIONS)
        print_menu(var)
      elif event.name == 'enter':
        return OPTIONS[var.selected]
      elif event.name == 'esc':
        return ''


def return_menu(var):
  print('\nPressione \033[1mesc\033[m para \033[1mVOLTAR\033[m.\nPressione \033[1menter\033[m para \033[1mCONFIRMAR\033[m.')
  while True:
    event = keyboard.read_event(suppress = True)
    if event.event_type == 'down':
      if event.name == 'esc':
        execute_program(var)
        return
      elif event.name == 'enter':
        code_label()
        print(f'O valor final à ser pago na condição "{var.condition}" selecionada, ficou \033[1mR${var.new_price:.2f}\033[m', end='')
        if var.installments >= 2:
          print(f' e o valor de cada parcela, em {var.installments}x: \033[1mR${var.ins_value:.2f}\033[m')
        else:
          print()
        print('\n\033[35mObrigado por usar nosso sistema! Até logo.\033[m')
        return


def execute_program(var):
  var.condition = payment_conditions(var)
  var.installments = 0
  if var.condition in OPTIONS:
    code_label()
    print(f'\033[33mValor do produto:\033[m \033[1mR${var.price:.2f}\033[m\n')
    if var.condition == OPTIONS[0]:
      print(f'{var.condition} você tem \033[33m10% de desconto\033[m no valor do produto.')
      var.new_price = var.price - (var.price * 10 / 100)
      print(f'Valor com desconto: \033[1mR${var.new_price:.2f}\033[m')
    elif var.condition == OPTIONS[1]:
      print(f'{var.condition} você tem \033[33m5% de desconto\033[m no valor do produto.')
      var.new_price = var.price - (var.price * 5 / 100)
      print(f'Valor com desconto: \033[1mR${var.new_price:.2f}\033[m')
    elif var.condition == OPTIONS[2]:
      print(f'{var.condition} o valor do produto permanece o mesmo.')
      var.new_price = var.price
      var.installments = 2
      var.ins_value = var.new_price / var.installments
      print(f'Valor do produto: \033[1mR${var.new_price:.2f}\033[m')
      print(f'Valor de cada parcela em {var.installments}x: \033[1mR${var.ins_value:.2f}\033[m')
    else:
      print(f'{var.condition} o valor do produto tem um \033[33macréscimo de 20%\033[m de juros.')
      var.new_price = var.price + (var.price * 20 / 100)
      while var.installments < 3:
        var.installments = int(input('Quantas parcelas? '))
        if var.installments >= 3:
          var.ins_value = var.new_price / var.installments
          print(f'Valor com juros: \033[1mR${var.new_price:.2f}\033[m')
          print(f'Valor de cada parcela em {var.installments}x: \033[1mR${var.ins_value:.2f}\033[m')
        else:
          print(f'Para 2x ou menos, selecione a opção "{OPTIONS[2]}"!')
    
    return_menu(var)
  
  return


if __name__ == '__main__':
  all_vars = Variables()
  get_price(all_vars)
  execute_program(all_vars)
