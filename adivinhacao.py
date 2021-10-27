import random

#adivinhar um número secreto
print('*********************************')
print('Bem vindo no jogo de adivinhação!')
print('*********************************')

# built in - já vem no python
#random - gerar um número aleatório - precisa ser imputado
#round - arredondar

numero_secreto = random.randrange(1,100) #0.0 e 1.0
total_de_tentativas = 0
rodada = 1
pontos = 100

print('Qual o nível de dificuldade? ')
print(' (1) Fácil (2) Médio (3) Difícil')

nivel = int(input('Defina o nível: '))

if(nivel == 1):
    total_de_tentativas = 20
elif(nivel == 2 ):
    total_de_tentivas = 10
else:
    total_de_tentativas = 5

print(numero_secreto)


#enquanto há tentativas:
#enquanto há tentativas execute este codigos (while). While como o if recebe uma condição. Mas o IF faz uma vez.
#o while executa enquanto ainda há esta condição.
# Começo com 0 e em cada laço (rodada vou diminuindo)

for rodada in range(1, total_de_tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))
    chute = int(input('Digite um numero entre 1 e 100: '))
    print('Vc digitou', chute)

    if(chute < 1 or chute > 100):
        print('Vc deve digitar um número entre 1 e 100!')
        continue
        #ele n para. se digitar menor do q 0 ele reinicia a iteração.


    acertou = chute == numero_secreto
    maior =   chute > numero_secreto
    menor =   chute < numero_secreto

    if(acertou):
        print('Vc acertou e fez {} pontos!'.format(pontos))
        break
        #break - ele sai do laço
    elif(maior):
        print('Vc chutou pra cima e fez {} pontos! '.format(pontos))
    elif(menor):
        print('Vc chutou pra baixo e fez {} pontos! '.format(pontos))
    pontos_perdidos = abs(numero_secreto - chute) # 40-20
    pontos = pontos - pontos_perdidos


print('Fim de jogo')


# Vc faz um laço empre incrementando o valor + 1

#FOR
    ##Com qual valor vc quer começar e até qual valor vc quer ir.
   # Range - define uma série de valores
# ex:. for rodada in range (1, 10): quero fazer um laço - (for - para), essa variavel (rodada) pega o valor dentro dessa serie (in range) de valores
    #pega do laço 1 até o 10
    #se quiser um step (1,10,2)
    
    #Se n usar o range [1, 2, 3, 4...] - o range define isso. lembra de colocar o range + 1''