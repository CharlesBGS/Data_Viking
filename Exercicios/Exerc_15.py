# Elabore um programa para calcular a hipotenusa de um triângulo.
#
# Dicas:
#
# Veja o módulo math (math.hypot)
#
# Utilize a seguinte fórmula: hipotenusa=(a²+b²)¹/2:

from math import hypot
print('Para calcular a hipotenusa, usamos a seguinte fómula: hipotenusa=(a²+b²)¹/2')
print('Sendo assim, preciso que você informe os valores dos catetos "a" e "b" para realizar esse calcúlo.')

a = float(input('Digite o valor do cateto "a": \n'))
b = float(input('Digite o valor do cateto "b": \n'))

hipotenusa = hypot(a,b)

print(f'O valor da hipotenusa é: {hipotenusa}. \n' )

# Após ver a solução apresentada pelo prof. Odemir, achei interessante acrescentar o seguinte trecho:

cateto_a = a
cateto_o = b

hipotenusa1=(cateto_a**2+cateto_o**2)**(1/2)  #forma de cálculo 1
print(f'Valor obtido pela aplicação do calculo descrito, sem o uso de biblioteca: {hipotenusa1}')


'''
from math import hypot

cateto_a=float(input('Digite o Cateto Adjacente: '))
cateto_o=float(input('Digite o Cateto Oposto: '))

hipotenusa1=(cateto_a**2+cateto_o**2)**(1/2)  #forma de cálculo 1
hipotenusa2=hypot(cateto_a,cateto_o)  #forma de cálculo 2

print(f'Hipotenusa: {hipotenusa1}')
print(f'Hipotenusa: {hipotenusa2}')

'''