from utils.utils import title, activity, clear_screen

import keyboard

OPTIONS = [' Pedra ', ' Papel ', 'Tesoura']


def code_label():
  title()
  activity('Jokenpô')


def computer_choice(): # Set the computer to choose randomly
  from random import randint
  choice = randint(1, 3)
  return choice


def print_menu(selected):
  clear_screen()
  code_label()

  print('=== Escolha ===')
  for i, option in enumerate(OPTIONS):
    if i == selected:
      print(f' >{option:^11}< ')
    else:
      print(f'  {option:^11}  ')
  print('='*15)
  print('\nPressione \033[1mesc\033[m para \033[1mSAIR\033[m')


def player_choice():
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
        return selected + 1
      elif event.name == 'esc':
        return 0


def repeat_menu():
  print()
  print('Para \033[1mJOGAR NOVAMENTE\033[m pressione \033[1menter\033[m.')
  print('Para \033[1mSAIR\033[m pressione \033[1mesc\033[m.')

  while True:
    event = keyboard.read_event(suppress = True)
    if event.event_type == 'down':
      if event.name == 'enter':
        jokenpo()
        return
      elif event.name == 'esc':
        clear_screen()
        code_label()
        print('Obrigado por jogar nosso jogo!\n')
        return


def jokenpo():
  computer = computer_choice()
  player = player_choice()

  if 1 <= player <= 3:
    clear_screen()
    code_label()
    print(f'Computador -> {OPTIONS[computer-1]} X {OPTIONS[player-1]} <- Jogador')
    if player == computer:
      print('TEMOS UM EMPATE!')
    elif (player == 1 and computer == 3) or (player == 2 and computer == 1) or (player == 3 and computer == 2):
      print('VOCÊ GANHOU!')
    else:
      print('VOCÊ PERDEU!')
    repeat_menu()

  return

if __name__ == '__main__':
  jokenpo()
