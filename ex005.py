#Faça um programa que leia um número inteiro e mostre na sua tela  seu sucessor e seu antecessor
n = int(input('Digite um número: '))
print('O antecessor do número {} é: {}'.format(n, n-1))
print('O sucessor desse número é {}: {}'.format(n, n+1))