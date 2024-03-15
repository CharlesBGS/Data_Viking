# Escreva um programa que peça dois números e apresente a divisão e multiplicação entre eles. A tela de apresentação deverá seguir o seguinte formato:
#
# "[número1]x[número2]=[multiplicação]"
#
# "[número1]/[número2]=[divisão]"


número1 = float(input('Digite um número: \n'))
número2 = float(input('Digite outro número: \n'))

multiplicação = número1 * número2
divisão = número1 / número2

print(f'O resuntado é: {número1} x {número2 }= {multiplicação}')
print(f'O resuntado é: {número1} / {número2} = {divisão}')

