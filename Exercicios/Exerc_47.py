# Utilizando estruturas de repetição escreva um programa que mostre os resultados
# da tabuada de multiplicação dos números entre 1 e 10, como segue.
'''
for i in range(1,11):
    print(f' 1 X {i} = {1*i}')
'''

# Depois de ver a solução do prof. Odemir, entendi o que era proposto:
# Um programa que mostrasse todas as tabuadas, começando na tabuada do 1 até a tabuada do 10.
# Por isso o termo 'estruturaS'.

for i in range(1,11):
    for num in range(1,11):
        print(f'{i} X {num} = {i*num}')

'''
# Solução apresentada pelo prof. Odemir:

for valor in range(1,11):
	for numero in range(1,11):
		print(f'{valor} x {numero} = {valor*numero}')

'''