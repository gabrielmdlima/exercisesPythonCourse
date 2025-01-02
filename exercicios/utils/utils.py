def title():
	from os import system
	system('cls')
	import __main__
	file = (__main__.__file__).split('\\')
	if 'ex' in file[len(file) - 1]:
		file = f' DESAFIO {file[len(file) - 1][2:5]} '
		print(f'\033[32m{file:=^33}\033[m')
	else:
		print('\033[31m*title() não aplicável*\033[m')


def activity(tarefa):
	tarefa = str(' '+tarefa+' ').upper()
	print(f'{tarefa:-^33}\n')
