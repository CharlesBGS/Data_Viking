# Escreva um programa que peça um número do usuário via método input e converta esse número para o formato float.

num = input('Digite um número: \n')
print(f'O número {num} convertido para float é: {float(num)}.')
# print(type(num))
'''
# A solução apresentada pelo prof. Odemir foi de realizar a conversão em uma linha de código separada,
# e depois, pedir somente o tipo de dado guardado na variável.
# No meu caso, se eu fizesse o mesmo, o retorno seria: <class 'str'>, pois não defini o tipo de dado que a variável
# deveria conter nem antes, nem depois de declara-la.

num=input('Digite um número:: ')
num=float(num)
print(type(num))

'''