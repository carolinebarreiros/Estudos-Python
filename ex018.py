#Faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ngulo

import math
n = float(input('Digite o ângulo de um ângulo: '))

s = math.sin(math.radians(n))
c = math.cos(math.radians(n))
t = math.tan(math.radians(n))

print('O valor do seno é {:.2f}:.\nO valor do coseno é {:.2f}.\nO valor da tangente é: {:.2f}'.format(s, c, t))
