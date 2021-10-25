#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
#Calcule e mostre o comprimento da hipotenusa

import math

cateto_oposto = float(input('Qual o valor do cateto oposto? '))
cateto_adj = float(input('Qual o valor do cateto adjacente? '))

hipotenusa = math.hypot(cateto_oposto, cateto_adj)

print('O cateto oposto é {}. O cateto adjacente é {}.\nComo  o quadrado da hipotenusa é igual a soma dos quadrados dos catetos, o valor da hipotenusa é: {:.2f}'.format(cateto_oposto, cateto_adj, hipotenusa))