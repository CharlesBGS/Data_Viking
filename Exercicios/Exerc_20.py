# Escreva um programa que peça um número inteiro do usuário e calcule e imprima a tabuada deste número.

num = int(input('Digite um número inteiro para saber sua tabuada: \n'))
print(f'A Tabuada do número {num} é: ')
for i in range(11):
    print(f'{num} X {i} = {i*num}');

'''

# Solução apresentada pelo prof. Odemir:
# A princípio pensei em fazer algo assim, mas preferi a criar algo usando o laço de repetição 'for'.

num=int(input('Digite um número inteiro: \n'))
print(f'Tabuada do número: {num}')
print(f'{num} x 1 = {num*1}')
print(f'{num} x 2 = {num*2}')
print(f'{num} x 3 = {num*3}')
print(f'{num} x 4 = {num*4}')
print(f'{num} x 5 = {num*5}')
print(f'{num} x 6 = {num*6}')
print(f'{num} x 7 = {num*7}')
print(f'{num} x 8 = {num*8}')
print(f'{num} x 9 = {num*9}')
print(f'{num} x 10 = {num*10}')

'''