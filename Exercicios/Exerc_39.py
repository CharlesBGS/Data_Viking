# Implemente uma calculadora simples com as operações aritméticas básicas.
# O usuário deverá especificar a operação desejada (+,-,*,/) e seguidamente inserir dois valores.
# Caso, o usuário escolha divisão e insira o valor do denominar 0 mostre uma mensagem personalizada.
# Para os demais casos, mostre na tela o resultado da operação desejada.

sinais = ['+','-','*','/']

operacao = input('Digite a operação que deseja realizar (+,-,*,/): ')
num1 = float(input('Digite o primeiro valor: '))
num2 = float(input('Digite o segundo valor: '))

if operacao in sinais:
    if operacao == '+':
        print(f' A soma dos valores {num1} + {num2} = {num1+num2}')
    elif operacao == '-':
        print(f' A subtração dos valores {num1} - {num2} = {num1-num2}')
    elif operacao == '*':
        print(f' A multiplicação dos valores {num1} * {num2} = {num1*num2}')
    elif operacao == '/' and num2 != 0:
        print(f' A divisão dos valores {num1} / {num2} = {num1/num2}')
    else:
        print(f'A operação não é válida. Não é possível dividir {num1} por {num2}')
else:
    print('Operação inválida!')

'''
# Solução apresentada pelo prof. Odemir:

operacao=input('Escolha a operação deseja: (+,-,*,/)')
if operacao in ['+','-','*','/']:
    num1=float(input('Número 1: '))
    num2=float(input('Número 2: '))
    if operacao=='+':
        print(f'{num1}+{num2}={num1+num2}')
    elif operacao=='-':
        print(f'{num1}-{num2}={num1-num2}')
    elif operacao=='*':
        print(f'{num1}*{num2}={num1*num2}')
    else:
        if num2==0:
            print('O denominador precisa ser diferente de zero.')
        else:
            print(f'{num1}/{num2}={num1/num2}')
else:
    print('Opção inválida.')

'''