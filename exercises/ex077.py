from utils.utils import title, activity
title()
activity('Vogais')

words = ('aprender', 'programar', 'linguagem', 'python',
         'curso', 'gratis', 'estudar', 'praticar',
         'trabalhar', 'mercado', 'programador', 'futuro')

for word in words:
  print(f'\nNa palavra {word.upper()} temos', end=' ')
  for letter in word:
    if letter in 'aeiou':
      print(letter, end=' ')

print('\n')
palavras = ('floresta', 'amigo', 'escola', 'computador', 'livro', 'codigo', 
         'internet', 'felicidade', 'ciencia', 'robos', 'natureza', 
         'filme', 'musica', 'tecnologia', 'aventura')

for word in palavras:
  print(f'Na palavra {word.upper()} temos', end=' ')
  if 'a' in word:
    for _ in range(word.count('a')):
      print('a', end=' ')
  if 'e' in word:
    for _ in range(word.count('e')):
      print('e', end=' ')
  if 'i' in word:
    for _ in range(word.count('i')):
      print('i', end=' ')
  if 'o' in word:
    for _ in range(word.count('o')):
      print('o', end=' ')
  if 'u' in word:
    for _ in range(word.count('u')):
      print('u', end=' ')
  print()
