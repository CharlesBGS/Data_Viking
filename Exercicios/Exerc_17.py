# Escreva um programa que peça um número do usuário e calcule o logaritmo deste número nas bases 10 e 2.
#
# Dica: utilize o módulo math.


'''
A princípio faria:
    from math import log10
    from math import log2
Porém é mais fácil importar math por completo.
'''

import math

num = int(input('Digite um número para que seja calculado o logaritmo dele nas bases 10 e 2: \n'))
print(f'O logaritmo do número {num} calculado na base 10 é {math.log10(num)}')
print(f'O logaritmo do número {num} calculado na base 2 é {math.log2(num)}')
print()
# Adicionei esse trecho após ver a solução do prof. Odemir, pois achei interessante o uso de math.log(variável,base).
print(math.log(num,10))
print(math.log(num,2))

'''

# Solução apresentada pelo prof. Odemir:

import math

num=float(input('Digite um número: '))
log1=math.log10(num)  #também podemos fazer: math.log(num,10)
log2=math.log(num,2)
print(f'O log de {num} na base 10 é {log1}')
print(f'O log de {num} na base 2 é {log2}')

'''