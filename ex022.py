# Crie um programa que leia o nome completo de uma pessoa e moste:
#O nome com todas as letras maiusculas
#o nome com tdas minusculas
#Qtas letras ao todo (sem considerar espaços)
#Quantas letras tem o primeiro nome
#strip elimina os espacos antes e depois

nome = str(input('Digite seu nome completo: ')).strip()
M = nome.upper()
m = nome.lower()
print('Todas as letras maiúsculas: {} '.format(M))
print('Todas as letras minúsculas: {} '.format(m))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
