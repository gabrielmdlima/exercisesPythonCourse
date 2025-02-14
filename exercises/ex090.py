from utils.utils import title, activity
title()
activity('Ficha de Aluno')

ficha = dict()

ficha['nome'] = str(input('Nome: '))
ficha['media'] = float(input(f'Média de {ficha["nome"]}: '))
print(f'Nome é igual à {ficha["nome"]}')
print(f'Média é igual à {ficha["media"]:.1f}')
print('Situação é igual à', 'Aprovado' if ficha['media'] >= 7 else 'Reprovado')
