# Escreva um programa que calcule a área de uma circunferência. O usuário deve digitar o valor do raio e ao final o programa deverá mostrar na tela a área da circunferência.
#
# Use a fórmula: área=pi*r² , em que pi é uma constante e r o raio da circunferência.
#
# Dica: você pode usar a biblioteca math para pegar a constante pi.

import math

pi = math.pi
raio = float(input('Digite o valor do Raio da circunferência que deseja calcular a área: \n'))
area = pi*(raio*raio)

print(f'A área da circunferência é de {area}')

'''

# A solução que o prof. Odemir apresentou fez algo que, por não conhecer a biblioteca, não fiz.
# Importa usando 'from math import pi', significa importar uma função da biblioteca direto para uma variável.
# Como não conhecia a biblioteca, primeiro a importei para depois vasculhar a função PI na lista de funções.

from math import pi
raio=float(input('Digite o valor do raio da circunferência: '))
print(f'Área da circunferência: {pi*raio**2:.2f}')

'''