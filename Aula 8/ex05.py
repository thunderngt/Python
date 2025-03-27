# Ordem de apresentação de um trabalho
from random import shuffle
aluno1 = str(input('Digite o nome do aluno 1: '))
aluno2 = str(input('Digite o nome do aluno 2: '))
aluno3 = str(input('Digite o nome do aluno 3: '))
aluno4 = str(input('Digite o nome do aluno 4: '))
pick = (aluno1, aluno2, aluno3, aluno4)
shuffle(pick)
print('A ordem escolhida foi {}, {}, {} e {}'.format(pick))