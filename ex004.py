#Faça um programa que leia algo pelo teclado e mostre seu tipo primitivo e todas as informaçoes possivel sobre ele

a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanumerico? ', a.isalnum())
print('Está em maiúscula? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizada?', a.istitle())