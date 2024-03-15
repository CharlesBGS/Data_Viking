# Utilizando estruturas de repetição escreva um programa que mostre os resultados
# da tabuada (multiplicação) de um número inserido pelo usuário.

num = int(input('Digite um número para ver sua tabuada: '))

for i in range(11):
    print(f'{num} X {i} = {i * num}');


'''
# Solução apresentada pelo prof. Odemir:

valor=int(input('Tabuada:'))
for num in range(1,11):
    print(f'{valor} x {num} = {valor*num}')

'''