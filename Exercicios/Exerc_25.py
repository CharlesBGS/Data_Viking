# Escreva um programa que receba dois números de ponto flutuante e mostre na tela o maior número digitado.
# Considere a possibilidade de o usuário digitar dois números iguais.

num1 = float(input('Digite o primeiro número com ponto flutuante: \n'))
num2 = float(input('Digite o segundo número com ponto flutuante: \n'))

if num1 < num2:
    print(f'O maior número entre os digitados é o segundo número digitado: {num2}')
elif num1 == num2:
    print(f'Os dois números são iguais')
else:
    print(f'O maior número entre os digitados é o primeiro número digitado: {num1}')

'''

# Solução apresentada pelo prof. Odemir:

n1=float(input('Valor 1 : '))
n2=float(input('Valor 2 : '))
if n1>n2:
    print(f'{n1}>{n2}')
elif n1==n2:
    print(f'{n1}={n2}')
else:
    print(f'{n1}<{n2}')

'''

