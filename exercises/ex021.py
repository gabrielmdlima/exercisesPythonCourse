from utils.utils import title, activity
title()
activity('Tocar mp3')

from playsound3 import playsound

def processo_atual(texto):
  print(f'\r{" " * 50}', end='', flush=True)
  print(f'\r{texto}', end='')

path = str(input('Qual o caminho mp3: ')).strip()
path = path.replace('\\', '/').replace('"', '')
file = path.split("/")[-1]
print(f'Playing audio: {file.capitalize()}\n')
processo_atual('\033[33mPlaying...\033[m')
playsound(path)
processo_atual('\033[32mDone!\033[m')
