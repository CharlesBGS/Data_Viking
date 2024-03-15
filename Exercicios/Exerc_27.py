# Escreva um programa que receba três números do usuário e mostre na tela o maior número digitado.

num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
num3 = float(input('Digite o terceiro número: '))

if num1>num2 and num1>num3:
    print(f'O primeiro número {num1} é o maior número digitado.')
elif num2>num1 and num2>num3:
    print(f'O segundo número {num2} é o maior número digitado.')
elif num3>num1 and num3>num2:
    print(f'O terceiro número {num3} é o maior número digitado.')
else:
    print(f'Os números {num1}, {num2} e {num3} são iguais.')

'''
# Solução apresentada pelo prof. Odemir:

numero1=float(input('Número 1: '))
numero2=float(input('Número 2: '))
numero3=float(input('Número 3: '))

if (numero1>=numero2) and (numero1>=numero3):
    print(f'Maior número: {numero1}')
elif (numero2>=numero1) and (numero2>=numero3):
    print(f'Maior número: {numero2}')
else:
    print(f'Maior número: {numero3}')

'''