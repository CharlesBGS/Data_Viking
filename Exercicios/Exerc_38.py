# Escreva um script para classificar um triângulo de acordo com o tamanho dos seus lados. Considere as seguintes informações:
# Triângulo equilátero: todos os lados possuem o mesmo tamanho;
# Trângulo escaleno: todos os lados possuem medidas diferentes;
# Triângulo isósceles: caracterizado por ter dois lados com o mesmo tamanho.

print('Classificador de Triângulos.')


cateto_a = float(input('Digite o valor do primeiro cateto: '))
cateto_b = float(input('Digite o valor do segundo cateto: '))
hipotenusa = float(input('Digite o valor da hipotenusa: '))

if cateto_a == cateto_b == hipotenusa:
    print('Este é um triângulo Equilátero.')
elif cateto_a != cateto_b != hipotenusa:
    print('Este é um Triângulo Escaleno.')
elif cateto_a == cateto_b or cateto_a == hipotenusa or cateto_b == hipotenusa:
    print('Este é um triângulo Isóceles.')

'''
# Solução apresentada pelo prof. Odemir:

ladoA=float(input('Lado A: '))
ladoB=float(input('Lado B: '))
ladoC=float(input('Lado C: '))
if ladoA==ladoB==ladoC:
    print('O triângulo é equilátero.')
elif ladoA==ladoB or ladoA==ladoC or ladoB==ladoC:
    print('O triângulo é isósceles.')
else:
    print('O triângulo é escaleno.')
    

'''