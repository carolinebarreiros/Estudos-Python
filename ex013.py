#Faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario, com 15% de aumento

salario_atual = float(input('Digite o salário atual do funcionário em reais: '))

#calculo de 15%

aumento = salario_atual * 0.15

novo_salario = salario_atual + aumento

print('O novo salário com 15% de aumento será {} reais'.format(novo_salario))