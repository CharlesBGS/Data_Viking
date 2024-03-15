 # Faça um programa que peça uma temperatura em Fahrenheit (F) e converta esta temperatura para grau Celsius (C), mostrando o resultado da conversão na tela.
 #
 # Use a fórmula: C = 5 * ((F-32) / 9).

f = float(input('Digite a temperatura em Fahrenheit que deseja converter para Graus Celsius: \n'))
c = 5*((f-32)/9)

print(f'{f} equivale a {c} ºC.')

print() # print vazio para 'pular uma linha' entre os prints.

# Após ver a solução do prof. Odemir, adequei a minha para:
print(f'Temperatura informada foi de {f:.2f} F.')
print(f'Equivalente a {c:.2f} ºC.')

'''

# Solução do prof. Odemir:
# Ele usou a string formatada para exibir somente 2 digitos após o ponto decimal.
# Para isso, passou o nome da variável, seguida de ':' (dois pontos), e por último o número de casas decimais.

f=float(input('Temperatura em Fahrenheit: \n'))
c=5*((f-32)/9)
print(f'{f:.2f}° F equivale a {c:.2f}° C .')

'''