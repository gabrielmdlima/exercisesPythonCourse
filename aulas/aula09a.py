frase = 'Curso em Vídeo Python'
print(frase)

print('\nFATIAMENTO')
print(frase[9])
print(frase[9:13])
print(frase[9:])
print(frase[9::2])
print(frase[:5])
print(frase[15:])

print('\nANÁLISE')
print(len(frase))
print(frase.count('o'))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

print('\nTRANSFORMAÇÃO')
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())

nova = '   Aprenda Python  '
print(f'\n{nova}.')

print(f'\n{nova.strip()}.')
print(f'\n{nova.rstrip()}.')
print(f'\n{nova.lstrip()}.')

print(f'\n{frase}')

print('\nDIVISÃO')
print(frase.split())
print(frase.split(' ', 1))

separada = frase.split()
print(f'\n{separada}')
print(separada[2])
print(separada[2][3])
junta = '-'.join(separada)
print(junta)
