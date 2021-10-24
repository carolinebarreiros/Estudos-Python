#DESAFIO 15
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e qtdade de dias pelos quais
#ele foi alugado. Calcule o preço a pagar. sabendo que o carro custa R$ 60.00 por dia e 0.15 reais por km rodada

dias = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos KM você rodou com o carro?' ))

#calculo da diária
diaria = dias * 60

#calculo por km
kmtotal = km * 0.15

print('Você ficou {} dias com o carro. E rodou {} KM. Logo, o total a ser pago é: R$ {:.2f}'.format(dias, km, diaria+kmtotal))