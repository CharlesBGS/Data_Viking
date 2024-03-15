# Faça um programa que recebe um número inteiro do usuário e calcule o fatorial deste número.
# Dica: utilize o módulo math do Python, especificamente math.fatorial.

from math import factorial

num = int(input('Digite um número inteiro para saber seu fatorial: \n'))

fatorial = factorial(num)

print(f'O fatorial do número {num} é: {fatorial}')


'''
# Solução apresentada pelo prof. Odemir:
# Editei a minha frase de input para solicitar ao usuário um número inteiro, pois é algo condicional para que seja feito
# o calculo de fatorial.

import math
num=int(input('Digite um número inteiro: '))
fatorial=math.factorial(num)
print(f'O fatorial de {num} é {fatorial}')


# Obs: Na matemática o número seguido do símbolo de exclamação (!) é conhecido como fatorial.
# por exemplo, x! (x fatorial). Vale ressaltar que, para que essa operação faça sentido, n é um número natural,
# ou seja, não calculamos fatorial de um número negativo, ou mesmo de um número decimal, ou de frações.

'''