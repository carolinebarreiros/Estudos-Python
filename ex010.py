#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
#considere um dolar = 3,27

r = float(input('Qual o valor em reais que vc tem na carteira? R$'))

#real para dolar

d = r / 3.27

print('Vc pode comprar {:.2f} US$'.format(d))