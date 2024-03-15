# Faça um programa que peça a base e a altura de um retângulo e calcule e mostre na tela a área e o perímetro.

print('Para calcular a área e o perímetro de um retângulo é necessário saber o valor de sua base e de sua altura.\n'
      'Digite a seguir os valores, conforme solicitado:')

base = float(input('Digite o valor da base do retângulo: \n'))
altura = float(input('Digite o valor da altura do retângulo: \n'))

area = base * altura
perimetro = (base + altura)*2

# Após ver a solução apresentada pelo prof. Odemir, achei interessante acrescentar a linha 13:
print(f'O retângulo digitado tem base {base} e altura {altura}.')
#
print('O cálculo da área aplicado é o seguinte: Base X Altura.')
print(f'A área do retângulo é de {area}')
print('O cálculo do perímetro aplicado é o seguinte: Base X 2 + Altura X 2.')
print(f'O períemtro do retângulo é de {perimetro}')


'''

base=float(input('Digite a base do retângulo: '))
altura=float(input('Digite a altura do retângulo: '))

area=base*altura
perimetro=2*base+2*altura

print(f'O retângulo digitado tem base {base} e altura {altura}.')
print(f'A área deste retângulo é: {area}')
print(f'O perímetro deste retângulo é: {perimetro}')

'''