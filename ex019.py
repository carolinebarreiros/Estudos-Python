#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que o ajude. Lendo o nome
#deles e escrevendo o nome do escolhido
import random

aluno1 = input('Digite o nome do aluno 1: ')
aluno2 = input('Digite o nome do aluno 2: ')
aluno3 = input('Digite o nome do aluno 3: ')
aluno4 = input('Digite o nome do aluno 4: ')

'''print('Os alunos são: {}, {}, {}, {}'.format(aluno1, aluno2, aluno3, aluno4))

s = random.random(aluno1, aluno2, aluno3, aluno4)

print('O aluno sorteado foi: {}'.format(s))'''

#criei uma lista
lista = [aluno4, aluno3, aluno2, aluno1]
s = random.choice(lista)
print('O aluno escolhido foi {}'.format(s))