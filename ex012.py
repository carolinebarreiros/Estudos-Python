#Faça um algoritmo que leia o preco de um produto e mostre seu novo preco com 5% de desconto

p = float(input('Digite o valor do produto em reais: R$'))

#cálculo do desconto de 5%

desconto = p*0.05
valor = p - desconto

print('O valor do seu produto com desconto será de R$ {:.2f}'.format(valor))