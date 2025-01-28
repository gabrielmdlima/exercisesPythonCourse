from utils.utils import title, activity
title()
activity('Tinta necessária')

alt = float(input('Qual a altura da parede? '))
larg = float(input('Qual a largura da parede? '))
area = alt * larg
print(f'Em uma parede de {area}m², seram necessários {(alt*larg)/2}L de tinta')
