# Escreva um programa que gere um número aleatório entre 1 e 100 e mostre na tela.
#
# Dica: utilize o módulo random.

import random

rand = random.randrange(1,100)
print(rand)

'''
# Solução apresentada pelo prof. Odemir:
# Ele usou o método .randint

import random
num=random.randint(1,100)
print(num)

# Diferenças:

Definição e Uso 'randrange()'
O randrange() método retorna um elemento selecionado aleatoriamente do intervalo especificado.

Sintaxe
random.randrange(start, stop, step)

Definição e Uso 'randint()'
O randint() método retorna um inteiro número elemento selecionado do intervalo especificado.
    Nota: Este método é um alias para randrange(start, stop+1).
    
Sintaxe
random.randint(start, stop)


'''