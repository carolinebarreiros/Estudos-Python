# Faça um programa que leia um numero inteiro qualquer e mostre na tela sua tabuada

n = int(input('Digite um número para ver sua tabuada: '))
t1 = n
t2 = n + t1
t3 = n + t2
t4 = n + t3
t5 = n + t4
t6 = n + t5
t7 = n + t6
t8 = n + t7
t9 = n + t8
t10 = n + t9



print('A tabuada do número digitado é:')
print('-' * 12)
print('{:2} X 1 = {}'.format(n, t1))
print('{:2} X 2 = {}'.format(n, t2))
print('{:2} X 3 = {}'.format(n, t3))
print('{:2} X 4 = {}'.format(n, t4))
print('{:2} X 5 = {}'.format(n, t5))
print('{:2} X 6 = {}'.format(n, t6))
print('{:2} X 7 = {}'.format(n, t7))
print('{:2} X 8 = {}'.format(n, t8))
print('{:2} X 9 = {}'.format(n, t9))
print('{:2} X 10 = {}'.format(n, t10))
print('_'* 12)