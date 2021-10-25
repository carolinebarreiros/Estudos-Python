#Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira

''''import math
n = float(input('Digite um número para ver sua porção inteira: '))
pi = math.floor(n)
print('O valor digitado foi: {}. A porção inteira desse número é: {}'.format(n, pi))'''''

'''OU
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, math.truc(num)))'''

'''from math import trunc
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, trunc(num)))'''

num = float(input('Digite um valor: '))
print('O valor digitado foi {} e sua porção inteira é {}'.format(num, int(num)))




