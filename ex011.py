#Faça um programa que leia a largura e a altura de uma parede em metros. Calcule sua area e a qtdade de tinta necessaria
#para pinta-la, sabendo que cada litro de tinta pinta uma area de 2metrosquadrados

l = float(input('Digite a largura da parede em metros: '))
a = float(input('Digite a altura da parede em metros: '))

#calculo da area da parede

area = l * a

print('Área da parede = {} metros quadrados'.format(area))

#calculo da tinta - sabendo q cada litro pinta 2 metrosquadrados

tinta = area/2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m2.'.format(l, a, area))
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))