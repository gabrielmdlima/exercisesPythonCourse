from utils.utils import title, activity, clear_screen
import keyboard
title()
activity('Binário, Octal e Hexadecimal')

OPTIONS = [' Binário ', ' Octal ', ' Hexadecimal ']


def code_label():
  clear_screen()
  title()
  activity('Binário, Octal e Hexadecimal')


def get_number():
  while True:
    num = int(input('Digite um número: '))
    if num <= 0:
      print('O número precisa ser maior que 0.')
    else:
      return num


def print_menu(num, selected):
  code_label()

  print(f'Número digitado: {num}\n')
  print('=== Base de conversão ===')
  for i, option in enumerate(OPTIONS):
    if i == selected:
      print(f' >{option:^21}< ')
    else:
      print(f'  {option:^21}  ')
  print('='*25)


def user_choice(num):
  selected = 0
  print_menu(num, selected)

  while True:
    event = keyboard.read_event(suppress = True)
    if event.event_type == 'down':
      if event.name == 'up':
        selected = (selected - 1) % len(OPTIONS)
        print_menu(num, selected)
      elif event.name == 'down':
        selected = (selected + 1) % len(OPTIONS)
        print_menu(num, selected)
      elif event.name == 'enter':
        return selected
      elif event.name == 'esc':
        return


def repeat_menu(num):
  print()
  print('Pressione \033[1menter\033[m para \033[1mVOLTAR\033[m')
  print('Pressione \033[1mesc\033[m para \033[1mSAIR\033[m')

  while True:
    event = keyboard.read_event(suppress=True)
    if event.event_type == 'down':
      if event.name == 'enter':
        execute_program(num)
        return
      elif event.name == 'esc':
        code_label()
        print('Até logo!\n')
        return



def execute_program(num):
  code_label()

  choice = user_choice(num)
  if choice in range(len(OPTIONS)):
    code_label()
    if choice == 0:
      print(f'O {num} convertido para BINÁRIO é {bin(num)[2:]}')
    elif choice == 1:
      print(f'O {num} convertido para OCTAL é {oct(num)[2:]}')
    else:
      print(f'O {num} convertido para HEXADECIMAL é {hex(num)[2:]}')

    repeat_menu(num)


  return

if __name__ == '__main__':
  num = get_number()
  execute_program(num)