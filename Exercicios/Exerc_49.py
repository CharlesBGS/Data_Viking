# Escreva um programa que peça ao usuário números entre 0-10.
# Se o usuário inserir um número fora desse intervalo o programa deverá finalizar com uma mensagem personalizada.

num_aceitos = ['0','1','2','3','4','5','6','7','8','9','10']
num = input('Digite um número inteiro entre 0 e 10: ')

while num in num_aceitos:
    if num in num_aceitos:
        print(f'{num} é uma opção válida.')
    num = input('Digite um número inteiro entre 0 e 10: ')
else:
    print('Fim do programa')


'''
Solução apresentada pelo prof. Odemir:
# Consideirei na minha solução que o usuário poderia digitar qualquer tipo de caractere, por isso adotei str na lista.
# O prof. assumiu apenas entradas int de 0-10, qualquer coisa além, quebra o programa.

num=0
while 0<=num<=10:
    num=int(input('Insira um número inteiro entre 0-10: '))
    if num<0 or num>10:
        print('Fim do programa.')

'''