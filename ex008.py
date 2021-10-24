#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

v = float(input('Digite um valor em metros: '))
c = v*100
m = v*1000

print('O valor digitado em metros equivale a {:.0f} centímetros'.format(c))
print('O valor digitado em metros equivale a {:.0f} milímetros'.format(m))