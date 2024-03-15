# Escreva um programa que peça um número inteiro do usuário e mostre se esse número é par ou ímpar.
# A mensagem na tela deverá seguir o seguinte formato:
#
# "O número [número] é [par/ímpar]"

num = int(input('Digite um número inteiro para saber se é Par ou Impar: '))

if num%2 == 0:
        print(f'O número {num} é Par.')
else:
    print(f'O número {num} é Impar.')

'''
# De início, pensei em criar uma variável para em seguida, verificar utilizando 'if' e 'else'.
# Porém percebi que economizaria linhas de código se não o fizesse.

num = int(input('Digite um número inteiro para saber se é Par ou Impar: '))

num_verificado = num%2
if num_verificado == 0:
    print(f'O número {num} é Par.')
else:
    print(f'O número {num} é Impar.')
'''

'''
# Solução apresentada pelo prof. Odemir:
# Se alinha ao meu pensamento de reduzir o número de linhas de código.

num=int(input('Número inteiro: '))
if num%2==0:
    print(f'O número {num} é par.')
else:
    print(f'O número é {num} é ímpar.')

'''