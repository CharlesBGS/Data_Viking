# Escreva um programa que verifique se um determinado número digitado pelo usuário é nulo, positivo ou negativo.

num = float(input('Digite um número: \n'))

if num == 0:
    print(f'O número {num} é Nulo.')
elif num > 0:
    print(f'O número {num} é Positivo.')
else:
    print(f'O número {num} é Negativo.')

'''

# Solução apresentada pelo prof. Odemir:

num=float(input('Digite um número: '))
if num>0:
    print('Número positivo.')
elif num==0:
    print('Número nulo.')
else:
    print('Número negativo.')

'''