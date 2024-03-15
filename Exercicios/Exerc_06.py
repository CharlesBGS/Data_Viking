# Faça um programa que calcule a raiz quadrada de um número. O usuário deve inserir um número e o programa
# deve mostrar na tela o resultado da raiz quadrada do número inserido.

import math

numero = float(input('Digite um número para saber qual é a sua raiz quadrada: \n'))
raiz = math.sqrt(numero)
print(f'A raiz quadrada do número {numero} é {raiz}')


'''
# Solução que o prof. Odemir apresentou: sem o uso de bibliotéca externa.

num=float(input('Digite um número: '))
print(f'A raiz quadrada de {num} é {num**(1/2)}')

'''